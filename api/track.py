from __future__ import annotations

import json
import time
from http.server import BaseHTTPRequestHandler


ALLOWED_EVENTS = {
    "page_view",
    "cv_loaded",
    "job_text_pasted",
    "analyze",
    "download_report",
    "print_report",
    "sample_loaded",
}


def clean_value(value):
    if isinstance(value, bool):
        return value
    if isinstance(value, int):
        return max(0, min(value, 1_000_000))
    if isinstance(value, float):
        return max(0, min(round(value, 3), 1_000_000))
    if isinstance(value, str):
        return value[:80]
    return None


class handler(BaseHTTPRequestHandler):
    def do_OPTIONS(self) -> None:
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self) -> None:
        length = int(self.headers.get("Content-Length", "0") or "0")
        raw = self.rfile.read(min(length, 4096))
        try:
            payload = json.loads(raw.decode("utf-8") or "{}")
        except json.JSONDecodeError:
            payload = {}

        event = str(payload.get("event", ""))[:40]
        if event not in ALLOWED_EVENTS:
            self.send_response(204)
            self.end_headers()
            return

        props = payload.get("props", {})
        if not isinstance(props, dict):
            props = {}

        safe_props = {}
        for key, value in props.items():
            key = str(key)[:40]
            cleaned = clean_value(value)
            if cleaned is not None:
                safe_props[key] = cleaned

        record = {
            "kind": "usage_event",
            "event": event,
            "ts": int(time.time()),
            "props": safe_props,
        }
        print(json.dumps(record, ensure_ascii=True), flush=True)

        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

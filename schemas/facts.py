from voluptuous import ALLOW_EXTRA, PREVENT_EXTRA, Any
from voluptuous import Schema

fact = Schema({
    'fact': str,
    "length": int
})

facts = Schema({
        "current_page": int,
        "data": [
            {
                "fact": str,
                "length": int
            }
        ],
        "first_page_url": str,
        "from": int,
        "last_page": int,
        "last_page_url": str,
        "links": [
            {
                "url": Any(str, None),
                "label": str,
                "active": bool
            }
        ],
        "next_page_url": str,
        "path": str,
        "per_page": str,
        "prev_page_url": Any(str, None),
        "to": int,
        "total": int
    },
        required=True,
        extra=PREVENT_EXTRA
    )

from flask import jsonify
from typing import Optional, List, Dict, Any, Union



def Response(message: str, data: Optional[Union[List, Dict, Any]] = None, status: int = 200) -> Dict:
    return jsonify({
        'message': message,
        'data': data
    }), status

from fastapi import APIRouter, Body, HTTPException
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/api/clicker/tap")
async def click(data = Body()):
    try:
        telegram_id = data['telegram_id']
        user_id = data['user_id']
        count = data['user_count']
        time = data['user_time']
        update_time = data['user_updatetime']
        upgrades = data['user_upgrades']
        energy = data['user_energy']
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing field: {str(e)}")
    
    return JSONResponse({'message': f'[INFO] ' + telegram_id + user_id + count + time + update_time + upgrades + energy})
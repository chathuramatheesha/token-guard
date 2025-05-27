from fastapi import APIRouter, status

router = APIRouter()


@router.post("/register", status_code=status.HTTP_200_OK)
async def register():
    pass

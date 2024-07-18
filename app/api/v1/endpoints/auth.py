from fastapi import APIRouter, Depends, HTTPException
router = APIRouter()


@router.get("")
def auth():
    return "This is Auth!"
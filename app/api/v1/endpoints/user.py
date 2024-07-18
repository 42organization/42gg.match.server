from fastapi import APIRouter, Depends, HTTPException
router = APIRouter()


@router.get("")
def users():
    return "This is User!"
from fastapi import APIRouter, Depends, HTTPException
router = APIRouter()


@router.get("")
def evaluations():
    return "This is Evaluations!"

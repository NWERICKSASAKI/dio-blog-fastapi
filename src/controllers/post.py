from fastapi import Response, Cookie, Header, FastAPI, status, APIRouter
from typing import Annotated
from datetime import datetime
from schemas.post import PostIn
from views.post import PostOut

router = APIRouter(prefix="/posts")


fake_db = [
    {"title":f"Criando uma aplicação com Django", "date":datetime.now(), "published": True},
    {"title":f"Criando uma aplicação com FastAPI", "date":datetime.now(), "published": True},
    {"title":f"Criando uma aplicação com Flask", "date":datetime.now(), "published": True},
    {"title":f"Criando uma aplicação com Starlett", "date":datetime.now(), "published": False},
]

# antigo '/posts/'
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=PostOut)
def create_post(post: PostIn):
    fake_db.append(post.model_dump()) # model_dump() -> retorna a apresentação desta classe como dicionário
    return post

@router.get("/", response_model=list[PostOut])
def read_posts(
    response: Response,
    limit: int ,
    published: bool,
    skip: int = 0,
    ads_id: Annotated[str | None, Cookie()] = None,
    user_agent: Annotated[str|None, Header()] = None):
    response.set_cookie(key='user', value='user@email.com')
    print(f'Cookie: {ads_id}')
    print(f'user-agent: {user_agent}')
    return [post for post in fake_db[skip : skip + limit] if post["published"] is published]


@router.get("/{framework}", response_model=PostOut)
def read_posts(framework: str):
    return {
        "posts":[
            {"title":f"Criando uma aplicação com {framework}", "date":datetime.now()},
            {"title":f"Internacionalizando uma app {framework}", "date":datetime.now()},
        ]
    }

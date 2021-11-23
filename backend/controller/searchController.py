import config
from flask import Blueprint, jsonify, request
from service.search_service import car_list, car_list_sorted, search
from sqlalchemy import create_engine

search_bp = Blueprint("search", __name__, url_prefix="/api")
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

# 초기 접속 시 url - 연비순 정렬
@search_bp.route("/car/list", methods=["GET"])
def get_car_List():
    if request.method == "GET":
        num = request.args.get("num", type=int, default=1)
        car = car_list(num)
        return jsonify(car), 200


@search_bp.route(
    "/search",
    methods=["GET"],
)
def get_search():
    if request.method == "GET":
        brand = request.args.get("brand")
        cost = request.args.get("cost")
        displacement = request.args.get("displacement")
        fuelEfficiency = request.args.get("fuelEfficiency")
        grade = request.args.get("grade")
        shape = request.args.get("shape")
        name = request.args.get("name")
        method = request.args.get("method")
        fuel = request.args.get("fuel")
        num = request.args.get("num", type=int, default=1)
        car = search(
            brand,
            cost,
            displacement,
            fuelEfficiency,
            grade,
            shape,
            name,
            method,
            fuel,
            num,
        )
        return jsonify(car), 200


@search_bp.route("/car/list/sorted", methods=["GET"])
def get_car_list_sorted():
    if request.method == "GET":
        sort_criteria = request.args.get("sort_criteria")
        num = request.args.get("num", type=int, default=1)
        car = car_list_sorted(sort_criteria, num)

        return jsonify(car), 200

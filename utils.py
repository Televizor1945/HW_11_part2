import json


__data = []


def load_candidates_from_json(path):
    """
    загружает json файл (наименование которого предадим аргументом в функцию), в котором анкеты кандидатов
    """
    global __data                       #Обозначили переменную __data, как глобальную переменную (вывели за область ф-ции)
    with open(path, "r", encoding="utf-8") as file:
        __data = json.load(file)
    return __data

def get_candidate(candidate_id):
    """
    Возвращает кандидата по id
    """
    for candidate in __data:
        if candidate["id"] == candidate_id:
            return {
                "name": candidate["name"],
                "position": candidate["position"],
                "picture": candidate["picture"],
                "skills": candidate["skills"],
            }
        return {"not_found": "такой кандидат не найден"}

def get_candidates_by_name(candidate_name):
    """
    функция ищет по совпадению в имени и фамилии (может искать по буквам в слове фамилии или имени)
    """
    count = 0
    candidate_list = []
    candidate_n = str(candidate_name)
    for candidate in __data:
        if candidate_n in candidate["name"]:
            candidate_list.append(candidate["name"])
            count += 1
    return count, candidate_list


def get_candidates_by_skill(skill_name):
    """
    функция, у кандидатов, ищет совпадению по навыкам
    """
    result = []
    count_skills = 0
    for candidate in __data:
        candidate_skills = candidate["skills"].lower().split(", ")
        if skill_name.lower() in candidate_skills:
            count_skills += 1
            result.append(candidate["name"])

    return count_skills, result


import json

from rapidfuzz import fuzz


def load(payload: str) -> object:
    return json.loads(payload)


def similarity_score(node_path: str, node_value: str, value: str) -> float:
    parts = node_path.split(".")
    # iterate through all the node names along the path and calculate the best match
    node_path_score = max([fuzz.ratio(part.lower(), value.lower()) for part in parts])

    node_value_score = fuzz.ratio(node_value.lower(), value.lower())
    return 0.7 * node_path_score + 0.3 * node_value_score


def traverse(obj: object, path: str, candidates: list, value: str, top_k: int) -> list:
    if type(obj) == dict:
        for key in obj:
            candidates = traverse(obj[key], path=f"{path}.{key}", candidates=candidates, value=value, top_k=top_k)
        return candidates
    elif type(obj) == list:
        for index, val in enumerate(obj):
            candidates = traverse(val, path=f"{path}[{index}]", candidates=candidates, value=value, top_k=top_k)
        return candidates
    elif type(obj) in [str, float, int, bool]:  # primitive types
        node_path = path
        node_value = str(obj)

        score = similarity_score(node_path, node_value, value)
        if len(candidates) < top_k:
            candidates.append((node_path, node_value, score))
        elif candidates[0][2] < score:
            candidates[0] = (node_path, node_value, score)

        return sorted(candidates, key=lambda x: x[2])
    else:
        raise RuntimeError(f"Not supported Type: {type(obj)}")


def search(payload: str, value: str) -> list:
    """
    fuzzy search for value inside a json payload
    the top_k json nodes will be returned based on the similarity scores between this value and
        - the path name to this node
        - the value contained in this node
    :param payload:
    :param value:
    :return:
    """
    candidates = []
    max_candidates = 5
    obj = load(payload)
    result = traverse(obj, path="$", candidates=candidates, value=value, top_k=max_candidates)
    return result



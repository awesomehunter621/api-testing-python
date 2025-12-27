import requests


BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts():
    url = f"{BASE_URL}/posts"
    r = requests.get(url, timeout=10)

    assert r.status_code == 200, f"Expected 200, got {r.status_code}"

    data = r.json()
    assert isinstance(data, list), "Expected a list of posts"
    assert len(data) > 0, "Expected at least one post"

    first = data[0]
    for key in ("userId", "id", "title", "body"):
        assert key in first, f"Missing key '{key}' in first post"

    print("✅ test_get_posts passed")


def test_get_single_post():
    url = f"{BASE_URL}/posts/1"
    r = requests.get(url, timeout=10)

    assert r.status_code == 200, f"Expected 200, got {r.status_code}"

    post = r.json()
    assert post["id"] == 1, "Expected id to be 1"
    assert isinstance(post["title"], str) and post["title"], "Expected a non-empty title"

    print("✅ test_get_single_post passed")


if __name__ == "__main__":
    test_get_posts()
    test_get_single_post()
    print("✅ All API checks passed")

def main(input: dict) -> dict:
    """
    Entry point for operato-runner module.
    Args:
        input (dict): Input data for the module.
    Returns:
        dict: Output/result data.
    """
    # 예시 처리
    result = {"message": f"Hello, {input.get('name', 'world')}!"}
    return result

if __name__ == "__main__":
    import sys, json
    if len(sys.argv) > 1:
        input_data = json.loads(sys.argv[1])
    else:
        input_data = {}
    output = main(input_data)
    print(json.dumps(output)) 
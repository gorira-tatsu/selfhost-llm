import torch
def main():
    print("Hello from selfhost-llm!")
    print(torch.cuda.is_available())


if __name__ == "__main__":
    main()

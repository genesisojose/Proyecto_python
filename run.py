from behave.__main__ import main as behave_main

if __name__ == "__main__":
    args = "src/features --tags=@smoke"
    behave_main(args)
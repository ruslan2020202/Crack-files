from program import Program


if __name__ == '__main__':
    try:
        program = Program()
        program.run()
    except KeyboardInterrupt:
        exit(0)

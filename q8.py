from typing import Optional, Sequence, Tuple

input_file = open("q8.txt")


def parse_instruction(instr: str) -> Tuple[str, int]:
    action, value = instr.split(" ")
    return (action, int(value))


raw_instructions = []
for line in input_file:
    raw_instructions.append(parse_instruction(line.strip()))


def run_program(instructions: Sequence[str]) -> Optional[int]:
    acc = 0
    lines_seen = set()
    lineno = 0
    while lineno not in lines_seen:
        if lineno >= len(instructions):
            lineno = -1
            break

        lines_seen.add(lineno)
        action, value = instructions[lineno]
        if action == "nop":
            lineno += 1
            continue
        elif action == "acc":
            acc += int(value)
            lineno += 1
            continue
        elif action == "jmp":
            lineno += int(value)
            continue

    if lineno == -1:
        return acc

    return None


for i, instruction in enumerate(raw_instructions):
    old_instr = instruction
    if old_instr[0] == "jmp":
        raw_instructions[i] = ("nop", old_instr[1])
    elif old_instr[0] == "nop":
        raw_instructions[i] = ("jmp", old_instr[1])

    result = run_program(raw_instructions)
    if result is not None:
        print("DID IT", result)
        break

    raw_instructions[i] = old_instr

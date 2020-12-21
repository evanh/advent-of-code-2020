from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Set, Sequence, Union

raw_rules = []
inputs = []
for line in open("q19.txt", "r"):
    if ":" in line:
        raw_rules.append(line.strip())
    elif line.strip() != "":
        inputs.append(line.strip())


class Rule(ABC):
    @abstractmethod
    def match(self, text: str) -> Set[str]:
        raise NotImplementedError


@dataclass
class Exact(Rule):
    text: str

    def match(self, text: str) -> Set[str]:
        if text.startswith(self.text):
            return {self.text}

        return set()

    def __repr__(self) -> str:
        return f"\"{self.text}\""


@dataclass
class Or(Rule):
    options: List[Rule]

    def match(self, text: str) -> Set[str]:
        matched = set()
        for rule in self.options:
            matched |= rule.match(text)

        return matched

    def __repr__(self) -> str:
        return f"({' | '.join(map(str, self.options))})"


@dataclass
class And(Rule):
    rules: List[Rule]

    def match(self, text: str) -> Set[str]:
        prefixes = self.rules[0].match(text)
        if len(prefixes) == 0:
            return prefixes

        for rule in self.rules[1:]:
            new = set()
            for prefix in prefixes:
                new_text = text[len(prefix):]
                matches = rule.match(new_text)
                for match in matches:
                    new.add(prefix + match)

            prefixes = new
            if len(prefixes) == 0:
                return prefixes

        return prefixes

    def __repr__(self) -> str:
        return f"({' '.join(map(str, self.rules))})"


rules = {}
for raw in raw_rules:
    rid, text = raw.split(":", 1)
    if text.strip().startswith("\""):
        rules[rid] = Exact(text.strip()[1:-1])
    elif "|" in text:
        parts = [p.strip() for p in text.split(" | ")]
        rules[rid] = {tuple(p.split(" ")) for p in parts}
    else:
        rules[rid] = tuple(text.strip().split(" "))


def build_tree(raw: Union[Set[Sequence[str]], Sequence[str], str, Exact]) -> Rule:
    if isinstance(raw, str):
        return build_tree(rules[raw])
    elif isinstance(raw, Exact):
        return raw
    elif isinstance(raw, tuple):
        return And([build_tree(r) for r in raw])
    else:
        return Or([build_tree(p) for p in raw])


def match(text: str, regex: Rule) -> bool:
    matches = regex.match(text)
    return any(text == match for match in matches)


regex = build_tree(rules["0"])
count = 0
for line in inputs:
    if match(line, regex):
        count += 1

print("Part 1", count)


@dataclass
class Rule8(Rule):
    rule42: Rule

    def match(self, text: str) -> Set[str]:
        prefixes = self.rule42.match(text)
        if len(prefixes) == 0:
            return prefixes

        prev = prefixes
        while len(prev) > 0:
            new = set()
            for prefix in prev:
                new_text = text[len(prefix):]
                if new_text == "":
                    continue

                matches = self.rule42.match(new_text)
                for match in matches:
                    new.add(prefix + match)

            prefixes |= new
            prev = new

        return prefixes


@dataclass
class Rule11(Rule):
    rule42: Rule
    rule31: Rule

    def match(self, text: str) -> Set[str]:
        prefixes = self.rule42.match(text)
        if len(prefixes) == 0:
            return prefixes

        levels = [prefixes]
        prev = prefixes
        while len(prev) > 0:
            new = set()
            for prefix in prev:
                new_text = text[len(prefix):]
                if new_text == "":
                    continue

                matches = self.rule42.match(new_text)
                for match in matches:
                    new.add(prefix + match)

            prev = new
            if len(new) > 0:
                prefixes |= new
                levels.append(new)

        full_matches = set()
        for i, matches in enumerate(levels):
            new = set()
            for prefix42 in matches:
                new_text = text[len(prefix):]
                prev = self.rule31.match(new_text)
                for j in range(i):
                    new = set()
                    if len(prev) == 0:
                        break

                    for prefix31 in prev:
                        text31 = new_text[len(prefix31):]
                        if len(text31) == 0:
                            continue

                        matches31 = self.rule31.match(text31)
                        for match in matches31:
                            new.add(prefix31 + match)

                    prev = new

                for prefix31 in prev:
                    full_matches.add(prefix42 + prefix31)

        return full_matches


def build_tree2(raw: Union[Set[Sequence[str]], Sequence[str], str, Exact]) -> Rule:
    if isinstance(raw, str):
        if raw == "8":
            return Rule8(build_tree2("42"))
        elif raw == "11":
            return Rule11(build_tree2("42"), build_tree2("31"))

        return build_tree2(rules[raw])
    elif isinstance(raw, Exact):
        return raw
    elif isinstance(raw, tuple):
        return And([build_tree2(r) for r in raw])
    else:
        return Or([build_tree2(p) for p in raw])


regex = build_tree2(rules["0"])
count = 0
for line in inputs:
    if match(line, regex):
        count += 1

print("Part 2", count)

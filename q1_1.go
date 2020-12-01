package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

func main() {
	file, err := os.Open("q1_1.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	data := []int{}
	for scanner.Scan() {
		text := scanner.Text()
		text = strings.TrimSpace(text)
		i, err := strconv.Atoi(text)
		if err != nil {
			log.Fatal(err)
		}
		data = append(data, i)
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	found := false
	for _, num1 := range data {
		for _, num2 := range data {
			if num1+num2 == 2020 {
				fmt.Printf("1: %d 2: %d = %d\n", num1, num2, num1*num2)
				found = true
				break
			}
		}

		if found {
			break
		}
	}

	found = false
	for _, num1 := range data {
		for _, num2 := range data {
			for _, num3 := range data {
				if num1+num2+num3 == 2020 {
					fmt.Printf("1: %d 2: %d 3: %d = %d\n", num1, num2, num3, num1*num2*num3)
					found = true
					break
				}
			}
			if found {
				break
			}
		}
		if found {
			break
		}
	}
}

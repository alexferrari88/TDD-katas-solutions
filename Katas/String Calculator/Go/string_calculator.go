package main

import (
	"fmt"
	"log"
	"regexp"
	"strconv"
	"strings"
)

func slice_sum(slice []string) (int, error) {
	var sum int
	for _, v := range slice {
		v, err := strconv.Atoi(v)
		if err != nil {
			return 0, err
		}
		sum += int(v)
	}

	return sum, nil
}

func create_regex_pattern(slice []string) string {
	for _, v := range slice {
		v = fmt.Sprintf("(?:%v)", v)
	}

	return strings.Join(slice, "|")
}

func Add(numbers string) int {
	if numbers == "" {
		return 0
	}

	separators := []string{"\n", ","}

	separators_regex := regexp.MustCompile(create_regex_pattern(separators))

	numbers_slice := separators_regex.Split(numbers, -1)
	numbers_sum, err := slice_sum(numbers_slice)

	if err != nil {
		log.Fatal(err)
	}

	return numbers_sum
}

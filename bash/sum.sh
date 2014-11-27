#!/bin/bash

# Usage: sum num1 num2

function sum()
{
    ((n=$1+$2))
}

sum $1 $2
echo $n

import sys
import os
import csv
import re


def deleteSpace(string):
    num = 0
    for i in range (len(string)):
        if (string[i] == " " and string[i+1] == " "):
            num = 1
            break
    if (num == 1):
        string = string.replace(" ", "")
        for i in range (len(string)):
            if (i+1 < len(string)and string[i].islower() and string[i+1].isupper()):
                string = string[:i+1] + " " + string[i+1:]
                break
    string = string.strip()
    return string

def writeFile(finalTable):
    fw = sys.stdout
    count = 1
    for i in range (1, len(finalTable)):
        title = "TABLE " + str(count) + ":\n"
        count += 1
        fw.write(title)
        for j in range (1, len(finalTable[i])):
            for k in range (len(finalTable[i][j])):
                if (k == len(finalTable[i][j])-1):
                    fw.write(finalTable[i][j][k] + "\n")
                else:
                    fw.write(finalTable[i][j][k] + ",")
        if (len(finalTable) > 2 and i < len(finalTable)-1):
            fw.write("\n")


def main():
    tableList = []
    itemList = []
    finalTable = []
    content = sys.stdin.readlines()
    result = ""
    for row in content:
        result += row
    result = result.replace("\n", "").replace("/t", "1\n").strip()
    count = 0
    for item in result.splitlines():
        if (re.search(r"able>",item)):
            finalTable.append(tableList)
            tableList  = []
        if (re.search(r"r>",item)):
            tableList.append(itemList)
            itemList = []
        if (re.search(r"<th(.*?)>(.*?)<1",item) or re.search(r"<td(.*?)>(.*?)<1",item)):
            if (re.search(r"<th(.*?)>(.*?)<1",item)):
                it = re.finditer(r"<th(.*?)>(.*?)<1",item)
                for match in it:
                    tempItem = match.group()
                    deleteItem = re.search(r"<th(.*?)>", tempItem).group()
                    tempItem = tempItem.replace(deleteItem, "").replace("<1", "")
                    tempItem = deleteSpace(tempItem)
                    itemList.append(tempItem)
            if (re.search(r"<td(.*?)>(.*?)<1",item)):
                it = re.finditer(r"<td(.*?)>(.*?)<1",item)
                for match in it:
                    tempItem = match.group()
                    deleteItem = re.search(r"<td(.*?)>", tempItem).group()
                    tempItem = tempItem.replace(deleteItem, "").replace("<1", "")
                    tempItem = deleteSpace(tempItem)
                    itemList.append(tempItem)
    for i in range(1, len(finalTable), 2):
        count = len(finalTable[i][1])
        for j in range(1, len(finalTable[i])):
            if (len(finalTable[i][j]) < count):
                for k in range(count-len(finalTable[i][j])):
                    finalTable[i][j].append("")
    writeFile(finalTable)

if __name__ == '__main__':
    main()


#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
typedef struct
{
    int32_t row;
    int32_t column;
    int32_t value;
} elements;
typedef struct
{
    char *name;
    elements element[1000];

} two_d_matrix;

two_d_matrix createMatrix();

void pauseKey();
void notExistMatrix();
void printMatrix(two_d_matrix matrix);
void printSubMatrix(two_d_matrix matrix);
void printTransposeMatrix(two_d_matrix matrix);
void printHadamardProductMatrix(two_d_matrix matrix1, two_d_matrix matrix2);
void printMultiplyyMatrix(two_d_matrix matrix1, two_d_matrix matrix2);
void printPowerMatrix(two_d_matrix matrix);
two_d_matrix MultiplyyMatrix(two_d_matrix matrix1, two_d_matrix matrix2);

int main()
{
    int32_t matrixCount = 0;
    int32_t option = 1;
    two_d_matrix myMatrix[20];

    // switch
    char *temp = NULL;
    char *temp2 = NULL;

    temp = malloc(sizeof(char) * 20);
    temp2 = malloc(sizeof(char) * 20);
    int32_t strLen = 0;
    int32_t checkName = 0;

    two_d_matrix tempMatrix;
    two_d_matrix temp2Matrix;

    while (option)
    {
        int32_t isPrint = 0;
        printf(" 1) 建立矩陣，每次使用會將前一次設置的清除\n");
        printf(" 2) 顯示指定矩陣內容\n");
        printf(" 3) 顯示指定submatrix內容\n");
        printf(" 4) 顯示指定矩陣轉置後的內容\n");
        printf(" 5) 顯示指定兩矩陣逐項乘績後的內容\n");
        printf(" 6) 顯示指定兩矩陣相乘後的內容\n");
        printf(" 7) 進行方陣次方計算\n");
        printf(" 0) 離開\n");
        printf("請輸入需要使用的功能(0 ~ 7)：");
        scanf("%d", &option);
        switch (option)
        {
        case 0:
            exit(0);
        case 1:
            printf("請輸入需要幾個矩陣(最多20): ");
            scanf("%d", &matrixCount);
            if (matrixCount > 20)
            {
                printf("Error:你輸入的數量超過20!\n");
                break;
            }
            for (int32_t i = 0; i < matrixCount; i++)
            {

                tempMatrix = createMatrix(i);
                myMatrix[i] = tempMatrix;
            }
            break;
        case 2:

            printf("請輸入你想顯示的矩陣名稱：");
            scanf("%s", temp);
            strLen = strlen(temp);
            for (int32_t i = 0; i < matrixCount; i++)
            {
                if (!strncmp(temp, myMatrix[i].name, strLen))
                {
                    tempMatrix = myMatrix[i];
                    printMatrix(tempMatrix);
                    isPrint = 1;
                }
            }
            if (!isPrint)
            {
                notExistMatrix();
            }
            break;
        case 3:
            printf("請輸入你想指定submatrix的矩陣名稱：");
            scanf("%s", temp);
            strLen = strlen(temp);
            for (int32_t i = 0; i < matrixCount; i++)
            {
                if (!strncmp(temp, myMatrix[i].name, strLen))
                {
                    tempMatrix = myMatrix[i];
                    printSubMatrix(tempMatrix);
                    isPrint = 1;
                    break;
                }
            }
            if (!isPrint)
            {
                notExistMatrix();
            }
            break;
        case 4:
            printf("請輸入你想指定轉置矩陣的矩陣名稱：");
            scanf("%s", temp);
            strLen = strlen(temp);
            for (int32_t i = 0; i < matrixCount; i++)
            {
                if (!strncmp(temp, myMatrix[i].name, strLen))
                {
                    tempMatrix = myMatrix[i];
                    printTransposeMatrix(tempMatrix);
                    isPrint = 1;
                }
            }
            if (!isPrint)
            {
                notExistMatrix();
            }
            break;
        case 5:
            printf("請輸入你想做逐項乘績的第一個矩陣名稱：");
            scanf("%s", temp);
            strLen = strlen(temp);
            checkName = 0;
            for (int32_t i = 0; i < matrixCount; i++)
            {
                if (!strncmp(temp, myMatrix[i].name, strLen))
                {
                    tempMatrix = myMatrix[i];
                    checkName = 1;
                }
            }
            if (!checkName)
            {
                notExistMatrix();
                break;
            }
            printf("請輸入你想做逐項乘績的第二個矩陣名稱：");
            scanf("%s", temp2);
            strLen = strlen(temp2);
            for (int32_t i = 0; i < matrixCount; i++)
            {
                if (!strncmp(temp2, myMatrix[i].name, strLen))
                {
                    temp2Matrix = myMatrix[i];
                    printHadamardProductMatrix(tempMatrix, temp2Matrix);
                    break;
                }
                else if (i == matrixCount)
                {
                    notExistMatrix();
                    break;
                }
            }
            break;
        case 6:
            printf("請輸入你想做矩陣乘積的第一個矩陣名稱：");
            scanf("%s", temp);
            strLen = strlen(temp);
            checkName = 0;
            for (int32_t i = 0; i < matrixCount; i++)
            {
                if (!strncmp(temp, myMatrix[i].name, strLen))
                {
                    tempMatrix = myMatrix[i];
                    checkName = 1;
                }
            }
            if (!checkName)
            {
                pauseKey();
                break;
            }
            printf("請輸入你想做矩陣乘積的第二個矩陣名稱：");
            scanf("%s", temp2);
            strLen = strlen(temp2);
            for (int32_t i = 0; i <= matrixCount; i++)
            {
                if (!strncmp(temp2, myMatrix[i].name, strLen))
                {
                    temp2Matrix = myMatrix[i];
                    printMultiplyyMatrix(tempMatrix, temp2Matrix);
                    break;
                }
                else if (i == matrixCount)
                {
                    pauseKey();
                    break;
                }
            }
            break;
        case 7:
            printf("請輸入你想做方陣次方的方陣名稱：");
            scanf("%s", temp);
            strLen = strlen(temp);
            for (int32_t i = 0; i < matrixCount; i++)
            {
                if (!strncmp(temp, myMatrix[i].name, strLen))
                {
                    tempMatrix = myMatrix[i];
                    printPowerMatrix(tempMatrix);
                    isPrint = 1;
                }
            }
            if (!isPrint)
            {
                notExistMatrix();
            }

            break;
        default:
            break;
        }
    }

    return 0;
}

two_d_matrix createMatrix(int32_t i)
{
    two_d_matrix my_two_d_matrix;
    int32_t rows, columns, value = 0;
    int32_t nonZeroElemnet = 1;
    char *buff;
    buff = malloc(30);
    my_two_d_matrix.name = malloc(30);

    printf("------------------------------------------------------------------------------------------\n");
    printf("請輸入第%d個矩陣的名稱:", i + 1);
    scanf("%s", buff);
    printf("請輸入陣列的列數(rows):");
    scanf("%d", &rows);
    my_two_d_matrix.element[0].row = rows;
    printf("請輸入陣列的行數(columns):");
    scanf("%d", &columns);
    my_two_d_matrix.element[0].column = columns;
    printf("------------------------------------------------------------------------------------------\n");

    // 輸入矩陣
    for (size_t i = 0; i < rows; i++)
    {
        for (size_t j = 0; j < columns; j++)
        {
            printf("請輸入[%zu][%zu]的值:", i, j);
            scanf("%d", &value);
            if (value)
            {
                my_two_d_matrix.element[nonZeroElemnet].row = i;
                my_two_d_matrix.element[nonZeroElemnet].column = j;
                my_two_d_matrix.element[nonZeroElemnet].value = value;

                nonZeroElemnet++;
            }

            if (i == rows - 1 && j == columns - 1)
            {
                printf("------------------------------------------------------------------------------------------\n");
                printf("------------------------------------------------------------------------------------------\n");
                printf("輸入結束，此矩陣為%dx%d矩陣\n", rows, columns);
                printf("------------------------------------------------------------------------------------------\n");
            }
            else if (j == columns - 1)
            {
                printf("------------------------------------------------------------------------------------------\n");
                printf("%zu列結束, 下一列為%zu\n", i, i + 1);
            }
            printf("------------------------------------------------------------------------------------------\n");
        }
    }

    my_two_d_matrix.name = buff;
    my_two_d_matrix.element[0].value = nonZeroElemnet - 1;

    return my_two_d_matrix;
}

void pauseKey()
{
    printf("按下Enter鍵以繼續\n");
    fflush(stdin);
    getchar();
}

void notExistMatrix()
{
    printf("------------------------------------------------------------------------------------------\n");
    printf("Error: 沒有您輸入的矩陣名稱\n");
    printf("------------------------------------------------------------------------------------------\n");
    pauseKey();
}

void printAllMatrix(int32_t matrixCount, two_d_matrix myMatrix[20])
{
    for (int32_t i = 0; i < matrixCount; i++)
    {
        printf("------------------------------------------------------------------------------------------\n");
        printf("-%d-| 名稱：%s | %dx%d矩陣\n", i + 1, myMatrix[i].name, myMatrix[i].element[0].row, myMatrix[i].element[0].column);
        printf("------------------------------------------------------------------------------------------\n");
    }
    pauseKey();
}

void printMatrix(two_d_matrix matrix)
{
    int32_t nonZeroElemt = 1;
    printf("此矩陣為%dx%d矩陣\n", matrix.element[0].row, matrix.element[0].column);
    printf("------------------------------------------------------------------------------------------\n");
    printf("------------------------------------------------------------------------------------------\n");
    for (size_t i = 0; i < matrix.element[0].row; i++)
    {
        for (size_t j = 0; j < matrix.element[0].column; j++)
        {
            if (!j)
            {
                printf("|");
            }
            if (matrix.element[nonZeroElemt].row == i && matrix.element[nonZeroElemt].column == j)
            {
                printf(" %-8d ", matrix.element[nonZeroElemt].value);
                nonZeroElemt++;
            }
            else
            {
                printf(" %-8d ", 0);
            }

            if (j == matrix.element[0].column - 1)
            {
                printf("|");
            }
        }
        printf("\n");
    }
    printf("------------------------------------------------------------------------------------------\n");
    printf("------------------------------------------------------------------------------------------\n");

    pauseKey();
}

void printSubMatrix(two_d_matrix matrix)
{
    int32_t subRowsStart, subRowsEnd, subColumnsStart, subColumnsEnd = 0;
    printf("請輸入子矩陣的列數起點(rows start):");
    scanf("%d", &subRowsStart);
    printf("請輸入子矩陣的列數終點(rows end):");
    scanf("%d", &subRowsEnd);
    if (subRowsEnd > matrix.element[0].row - 1 || subRowsStart > matrix.element[0].row - 1)
    {
        printf("\nError:你輸入的子矩陣列數大於母矩陣列數!!\n");
        exit(0);
    }
    printf("請輸入子矩陣的行數起點(columns start):");
    scanf("%d", &subColumnsStart);
    printf("請輸入子矩陣的行數終點(columns end):");
    scanf("%d", &subColumnsEnd);
    if (subColumnsEnd > matrix.element[0].column - 1 || subColumnsStart > matrix.element[0].column - 1)
    {
        printf("\nError:你輸入的子矩陣行數大於母矩陣行數!!\n");
        exit(0);
    }
    printf("------------------------------------------------------------------------------------------\n");
    printf("------------------------------------------------------------------------------------------\n");

    for (size_t i = subRowsStart; i <= subRowsEnd; i++)
    {
        for (size_t j = subColumnsStart; j <= subColumnsEnd; j++)
        {
            int32_t nonZeroElement = 1;
            if (j == subColumnsStart)
            {
                printf("|");
            }

            for (size_t k = 1; k <= matrix.element[0].value; k++)
            {
                if (matrix.element[k].row == i && matrix.element[k].column == j)
                {
                    printf(" %-8d ", matrix.element[k].value);
                    nonZeroElement = 0;
                }
            }

            if (nonZeroElement)
            {
                printf(" %-8d ", 0);
            }

            if (j == subColumnsEnd)
            {
                printf("|");
            }
        }
        printf("\n");
    }
    printf("------------------------------------------------------------------------------------------\n");
    printf("------------------------------------------------------------------------------------------\n");

    pauseKey();
}

void printTransposeMatrix(two_d_matrix matrix)
{
    int32_t nonZeroElemt = 0;
    printf("此矩陣轉置矩陣為%dx%d矩陣\n", matrix.element[0].column, matrix.element[0].row);
    printf("------------------------------------------------------------------------------------------\n");
    printf("------------------------------------------------------------------------------------------\n");
    for (size_t i = 0; i < matrix.element[0].column; i++)
    {
        for (size_t j = 0; j < matrix.element[0].row; j++)
        {
            int32_t nonZeroElement = 1;
            if (!j)
            {
                printf("|");
            }

            for (size_t k = 1; k <= matrix.element[0].value; k++)
            {
                if (matrix.element[k].column == i && matrix.element[k].row == j)
                {
                    printf(" %-8d ", matrix.element[k].value);
                    nonZeroElement = 0;
                }
            }

            if (nonZeroElement)
            {
                printf(" %-8d ", 0);
            }

            if (j == matrix.element[0].row - 1)
            {
                printf("|");
            }
        }
        printf("\n");
    }
    printf("------------------------------------------------------------------------------------------\n");
    printf("------------------------------------------------------------------------------------------\n");

    pauseKey();
}

void printHadamardProductMatrix(two_d_matrix matrix1, two_d_matrix matrix2)
{
    if (matrix1.element[0].column != matrix2.element[0].column || matrix1.element[0].row != matrix2.element[0].row)
    {
        printf("兩個矩陣行列數不相等，無法做逐項乘績\n");
        pauseKey();
    }

    printf("逐項乘績結果為：\n");
    printf("------------------------------------------------------------------------------------------\n");

    for (size_t i = 0; i < matrix1.element[0].row; i++)
    {
        for (size_t j = 0; j < matrix1.element[0].column; j++)
        {
            int32_t matrixOneNonZeroElement, matrixTwoNonZeroElement = 0;
            if (!j)
            {
                printf("|");
            }
            for (size_t k = 1; k <= matrix1.element[0].value; k++)
            {
                if (matrix1.element[k].row == i && matrix1.element[k].column == j)
                {
                    matrixOneNonZeroElement = k;
                }
            }
            for (size_t k = 1; k <= matrix2.element[0].value; k++)
            {
                if (matrix2.element[k].row == i && matrix2.element[k].column == j && matrixOneNonZeroElement)
                {
                    printf(" %-8d ", matrix2.element[k].value * matrix1.element[matrixOneNonZeroElement].value);
                    matrixTwoNonZeroElement = 1;
                }
            }
            if (!matrixTwoNonZeroElement)
            {
                printf(" %-8d ", 0);
            }

            if (j == matrix1.element[0].column - 1)
            {
                printf("|");
            }
        }
        printf("\n");
    }
    printf("------------------------------------------------------------------------------------------\n");
    printf("------------------------------------------------------------------------------------------\n");
    pauseKey();
}

void printMultiplyyMatrix(two_d_matrix matrix1, two_d_matrix matrix2)
{
    if (matrix1.element[0].column != matrix2.element[0].row)
    {
        printf("前者的行數不等於後者的列數，無法做矩陣乘法\n");
        pauseKey();
    }

    printf("%dx%d矩陣與%dx%d矩陣相乘為%dx%d矩陣\n", matrix1.element[0].row, matrix1.element[0].column, matrix2.element[0].row, matrix2.element[0].column, matrix1.element[0].row, matrix2.element[0].column);
    printf("矩陣相乘績結果為：\n");
    printf("------------------------------------------------------------------------------------------\n");

    for (size_t i = 0; i < matrix1.element[0].row; i++)
    {
        for (size_t j = 0; j < matrix2.element[0].column; j++)
        {
            int32_t addElement = 0;
            for (size_t k = 1; k <= matrix1.element[0].value; k++)
            {
                if (matrix1.element[k].row == i)
                {
                    for (size_t t = 1; t <= matrix2.element[0].value; t++)
                    {
                        if (matrix2.element[t].column == j)
                        {
                            if (matrix1.element[k].column == matrix2.element[t].row)
                            {
                                addElement += matrix1.element[k].value * matrix2.element[t].value;
                            }
                        }
                    }
                }
            }

            if (!j)
            {
                printf("|");
            }
            printf(" %-8d ", addElement);
            if (j == matrix2.element[0].column - 1)
            {
                printf("|");
            }
        }
        printf("\n");
    }
    printf("------------------------------------------------------------------------------------------\n");
    printf("------------------------------------------------------------------------------------------\n");
    pauseKey();
}

two_d_matrix MultiplyyMatrix(two_d_matrix matrix1, two_d_matrix matrix2)
{
    two_d_matrix multiply_two_d_matrix;
    int32_t rows, columns, value = 0;
    int32_t nonZeroElemnet = 1;
    char *buff;
    buff = malloc(30);
    if (matrix1.element[0].column != matrix2.element[0].row)
    {
        printf("前者的行數不等於後者的列數，無法做矩陣乘法\n");
        pauseKey();
    }

    multiply_two_d_matrix.element[0].row = matrix1.element[0].row;
    multiply_two_d_matrix.element[0].column = matrix2.element[0].column;

    for (size_t i = 0; i < matrix1.element[0].row; i++)
    {
        for (size_t j = 0; j < matrix2.element[0].column; j++)
        {
            int32_t addElement = 0;
            for (size_t k = 1; k <= matrix1.element[0].value; k++)
            {
                if (matrix1.element[k].row == i)
                {
                    for (size_t t = 1; t <= matrix2.element[0].value; t++)
                    {
                        if (matrix2.element[t].column == j)
                        {
                            if (matrix1.element[k].column == matrix2.element[t].row)
                            {
                                addElement += matrix1.element[k].value * matrix2.element[t].value;
                            }
                        }
                    }
                }
            }

            if (addElement)
            {
                multiply_two_d_matrix.element[nonZeroElemnet].row = i;
                multiply_two_d_matrix.element[nonZeroElemnet].column = j;
                multiply_two_d_matrix.element[nonZeroElemnet].value = addElement;
                multiply_two_d_matrix.element[0].value++;
                nonZeroElemnet++;
            }
        }
    }
    return multiply_two_d_matrix;
}

void printPowerMatrix(two_d_matrix matrix)
{
    two_d_matrix temp_matrix;
    two_d_matrix ret_matrix;
    int32_t exp = 0;
    int32_t expNow = 2;
    printf("請輸入方陣次方數(>=2):");
    scanf("%d", &exp);
    if (exp < 2)
    {
        printf("------------------------------------------------------------------------------------------\n");
        printf("Error: 您輸入的次方數小於2\n");
        printf("------------------------------------------------------------------------------------------\n");
    }

    temp_matrix = MultiplyyMatrix(matrix, matrix); // matrix square
    if (exp == 2)
    {
        ret_matrix = temp_matrix;
    }
    else if (exp % 2 == 0)
    {
        for (size_t i = 0; expNow == exp; i++)
        {
            temp_matrix = MultiplyyMatrix(temp_matrix, temp_matrix);
            expNow *= 2;
        }
    }

    printMatrix(temp_matrix);
}
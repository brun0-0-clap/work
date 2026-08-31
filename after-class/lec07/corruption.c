#include <stdio.h>
typedef struct {
    int id;
    int scores[3];
} Student;

Student students[2];

void init() {
    students[0].id = 1001;
    students[0].scores[0] = 85;
    students[0].scores[1] = 92;
    students[0].scores[2] = 78;

    students[1].id = 1002;
    students[1].scores[0] = 90;
    students[1].scores[1] = 88;
    students[1].scores[2] = 95;
}

void curve_scores(int student_idx, int curve) {
    // BUG：循环 i<4，数组只有3个元素 scores[0‑2]，越界改写相邻内存（students[1].id）
    for (int i = 0; i < 4; i++) {
        students[student_idx].scores[i] += curve;
    }
}

int main() {
    init();
    printf("=== Initial state ===\n");
    printf("Student 0: id=%d\n", students[0].id);
    printf("Student 1: id=%d\n", students[1].id);

    curve_scores(0, 5);

    printf("\n=== After curving ===\n");
    printf("Student 0: id=%d\n", students[0].id);
    printf("Student 1: id=%d\n", students[1].id);

    if (students[1].id != 1002) {
        printf("\nERROR: Student 1's ID was corrupted! Expected 1002, got %d\n", students[1].id);
        return 1;
    }
    return 0;
}

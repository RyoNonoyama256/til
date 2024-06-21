#include <iostream>
#include <cstring>

/* start:基本的な構造体とポインタの利用 */
struct Student { 
    char name[50];
    int age;
    float grade;
    int* id;
};

void showStudentInfo(Student* stu){
    std::cout << "=====\nName: " << (*stu).name << std::endl;
    std::cout << "Age: " << stu -> age << std::endl;
    std::cout << "Grade: " << stu -> grade << std::endl;
    std::cout << "id: " << *(stu -> id) << std::endl;
}

void makeStudentAndShowInfo(){
    /* student1 */
    Student stu1 = {};
    strcpy(stu1.name, "Tanaka");
    stu1.age = 18;
    stu1.grade = 1.5;
    stu1.id = new int;
    *(stu1.id) = 101;
    showStudentInfo(&stu1);
    delete stu1.id;
    stu1.id = nullptr;

    /* student2 */
    Student stu2 = {
        "Yamada",
        16,
        0.5,
        nullptr
    };
    stu2.id = new int;
    *(stu2.id) = 102;
    showStudentInfo(&stu2);
    delete stu2.id;
    stu2.id = nullptr;
}
/* end:基本的な構造体とポインタの利用 */


int main(){
    makeStudentAndShowInfo();
    return 0;
}

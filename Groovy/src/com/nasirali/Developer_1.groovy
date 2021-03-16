package com.nasirali
@groovy.transform.ToString //to transform object (new) to string
class Developer_1 {
    String first
    String last
    def languages=[]

    void work(){
        println "$first $last is working..."
    }
}

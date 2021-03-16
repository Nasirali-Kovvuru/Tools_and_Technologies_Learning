package com.nasirali
@groovy.transform.ToString //to transform object (new) to string
class Tweet_2 {
    String username
    String text
    Integer retweets
    Integer favorites
    Date createdOn

    //constructor
    Tweet_2(String user, String message){
        username = user
        text = message
        retweets = 0
        favorites = 0
        createdOn = new Date()

    }
    void addToRetweets(){
        retweets += 1
    }
    void addToFavorites(){
        favorites += 1
    }
}

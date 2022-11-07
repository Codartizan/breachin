package org.example;

import com.google.gson.Gson;
import io.restassured.response.Response;

import static io.restassured.RestAssured.given;

public class Dependent {

    public static void main(String[] args) {
//            Response response = RestAssured.get("https://api.github.com/search/code?q=def +in:file+repo:django/django");
        Response resp = given().header("Authorization", "token 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")
                .header("Accept", "application/vnd.github.v3+json")
                .param("q", "def +in:file+repo:django/django")
                .get("https://api.github.com/search/code");
        String jsonStr = resp.body().asString();
        System.out.println(resp.body().prettyPrint());

        Gson gson = new Gson();
        org.example.searchCode.Response respObj = gson.fromJson(jsonStr, org.example.searchCode.Response.class);

        System.out.println(respObj.getItems().size());

        respObj.getItems().forEach(r -> System.out.println(r.getName()));
    }



}

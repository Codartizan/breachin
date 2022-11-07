package org.example;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class GetAllCodeUnitsFromList {

    public static void main(String[] args) throws IOException {
        String path = "/Users/tshi/researchProjs/scipy/scipy-1.8.0/";
        Path start = Paths.get(path);

        List<String> classCount = new ArrayList<>();
        List<String> funcCount = new ArrayList<>();
        List<String> moduleCount = new ArrayList<>();

        List<String> collect = Files.readAllLines(Paths.get("/Users/tshi/IdeaProjects/breachin/src/main/resources/django_remove"));

        collect.forEach(f -> {
//                System.out.println(f);
            if (f.endsWith(".py") && !f.contains("test") && !f.contains("doc") && !f.contains("example")) {
                try {
                    String content = GetAllCodeUnitsFromFolder.readFileToString(f);
                    if (!content.contains("class ") && !content.contains("def ")) {
                        System.out.println(" Module : " + f);
                        moduleCount.add(f);
                    }
                    Pattern MY_PATTERN = Pattern.compile("def (\\w+)\\s*\\((.*?)\\):");
                    Matcher m = MY_PATTERN.matcher(content);
                    while(m.find()) {
                        System.out.println(m.group() + " in file : " + f);
                        funcCount.add(m.group());
                    }
                    Pattern MY_PATTERN2 = Pattern.compile("class (\\w+)\\s*\\((.*?)\\):");
                    Matcher m2 = MY_PATTERN2.matcher(content);
                    while(m2.find()) {
                        System.out.println(m2.group() + " in file : " + f);
                        classCount.add(m2.group());
                    }
                    Pattern MY_PATTERN3 = Pattern.compile("class (\\w+)\\s*:");
                    Matcher m3 = MY_PATTERN3.matcher(content);
                    while(m3.find()) {
                        System.out.println(m3.group() + " in file : " + f);
                        classCount.add(m3.group());
                    }
            } catch (IOException e) {
                    throw new RuntimeException(e);
            }
            }
        });

        System.out.println("Total class number:" + (int) classCount.stream().distinct().count());
        System.out.println("Total function number:" + (int) funcCount.stream().distinct().count());
        System.out.println("Total module number:" + (int) moduleCount.stream().distinct().count());
    }
}

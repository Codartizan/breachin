package org.example;

import java.io.FileInputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class GetAll {

    public static void main(String[] args) throws IOException {
        String path = "/Users/tshi/researchProjs/django/django-3.2.14/";
        Path start = Paths.get(path);

        AtomicInteger classCount = new AtomicInteger();
        AtomicInteger funcCount = new AtomicInteger();
        AtomicInteger moduleCount = new AtomicInteger();
        try (Stream<Path> stream = Files.walk(start, Integer.MAX_VALUE)) {
            List<String> collect = stream
                    .map(String::valueOf)
                    .sorted()
                    .collect(Collectors.toList());

            collect.forEach(f -> {
                if (f.endsWith(".py") && !f.contains("test")) {
                    try {
                        String content = readFileToString(f);
                        if (!content.contains("class ")) {
                            moduleCount.getAndIncrement();
                        }
                        Pattern MY_PATTERN = Pattern.compile("def (\\w+)\\s*\\((.*?)\\):");
                        Matcher m = MY_PATTERN.matcher(content);
                        while(m.find()) {
                            System.out.println(m.group());
                            funcCount.getAndIncrement();
                        }
                        Pattern MY_PATTERN2 = Pattern.compile("class (\\w+)\\s*\\((.*?)\\):");
                        Matcher m2 = MY_PATTERN2.matcher(content);
                        while(m2.find()) {
                            classCount.getAndIncrement();
                        }
                        Pattern MY_PATTERN3 = Pattern.compile("class (\\w+)\\s*:");
                        Matcher m3 = MY_PATTERN3.matcher(content);
                        while(m3.find()) {
                            classCount.getAndIncrement();
                        }
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                } else {
//                    System.out.println(f);
                }
            });
        }

        System.out.println("Total class number:" + classCount);
        System.out.println("Total function number:" + funcCount);
        System.out.println("Total module number:" + moduleCount);

    }

    public static String readFileToString(String fileName) throws IOException {
        FileInputStream fis = new FileInputStream(fileName);
        byte[] buffer = new byte[10];
        StringBuilder sb = new StringBuilder();
        while (fis.read(buffer) != -1) {
            sb.append(new String(buffer));
            buffer = new byte[10];
        }
        fis.close();

        return sb.toString();
    }
}

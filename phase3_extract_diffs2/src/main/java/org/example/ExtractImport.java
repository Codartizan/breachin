package org.example;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;
import java.util.stream.Stream;

import static org.example.GetAllCodeUnitsFromFolder.readFileToString;

public class ExtractImport {

    public static void main(String[] args) throws IOException {
        String path = "/Users/tshi/researchProjs/click/click-7.1.0/";
        Path start = Paths.get(path);

        List<String> result = new ArrayList<>();

        try (Stream<Path> stream = Files.walk(start, Integer.MAX_VALUE)) {
            List<String> collect = stream
                    .map(String::valueOf)
                    .sorted()
                    .collect(Collectors.toList());

            collect.forEach(f -> {
                if (f.endsWith(".py") && !f.contains("test") && !f.contains("example") && !f.contains("docs")) {
                    try {
                        String content = readFileToString(f);
                        if (content.contains(" import pandas as pd")) {
                            System.out.println(f);
                            Pattern MY_PATTERN = Pattern.compile("pd\\.(.*)");
                            Matcher m = MY_PATTERN.matcher(content);
                            while (m.find()) {
                                result.add(m.group());
//                                System.out.println(m.group());
                            }
                        }
                    } catch (IOException e) {
                        throw new RuntimeException(e);
                    }
                }
            });
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        System.out.println("Total occurrence: " + result.size());
        System.out.println("Total type usage: " + (int)result.stream().distinct().count());

        result.stream().distinct().forEach(System.out::println);


    }
}

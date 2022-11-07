package org.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

/**
 * Hello world!
 *
 */
public class DiffCompare
{
    public static void main( String[] args ) throws IOException {
        String file = "/Users/tshi/IdeaProjects/breachin/src/main/resources/matplotlib_remained_diff";

        List<String> list = new ArrayList<>();

        try (BufferedReader br = Files.newBufferedReader(Paths.get(file))) {
            //br returns as stream and convert it into a List
            list = br.lines().collect(Collectors.toList());
        } catch (IOException e) {
            e.printStackTrace();
        }

        ArrayList<ArrayList<String>> fileDiffs = new ArrayList<>();

//        int i = 0;
        for (int i = 0; i < list.size(); i++) {
            if (list.get(i).startsWith("('")) {
//                String delim = "\n";
                int k = i+1;
                ArrayList<String> arr = new ArrayList<>();
                arr.add(list.get(i));
//                arr.add(delim);
                while (!list.get(k).startsWith("('") && k < list.size() - 1) {
                    arr.add(list.get(k));
//                    arr.add(delim);
                    k++;
                }
                fileDiffs.add(arr);
            }
//            i++;
        }

        System.out.println("Remained file changes size: " + fileDiffs.size());

        List<String> mc = new ArrayList<>();
        List<String> ac = new ArrayList<>();
        List<String> dc = new ArrayList<>();

        for (ArrayList<String> fdarr: fileDiffs) {
            for (String line : fdarr) {
                if (!hasClass(line).isBlank()) {
//                    System.out.println(fdarr.get(0));
//                    System.out.println(line.charAt(0) + hasClass(line));
                    String f = "Class %s in file %s is %s";
                    int start = fdarr.indexOf(line) + 1;
                    StringBuilder status = new StringBuilder();
                    while (start < fdarr.size() - 1) {
                        if (hasClass(fdarr.get(start)).isBlank()) {
                            status.append(fdarr.get(start));
                            start++;
                        } else {
                            break;
                        }
                    }
                    if (status.toString().contains("-") && status.toString().contains("+")) {
                        System.out.printf((f) + "%n", line.charAt(0) + hasClass(line), fdarr.get(0), "modified");
                        mc.add(hasClass(line));
                    } else if (status.toString().contains("-") && !status.toString().contains("+")) {
                        System.out.printf((f) + "%n", line.charAt(0) + hasClass(line), fdarr.get(0), "deleted");
                        dc.add(hasClass(line));
                    } else if (!status.toString().contains("-") && status.toString().contains("+")) {
                        System.out.printf((f) + "%n", line.charAt(0) + hasClass(line), fdarr.get(0), "added");
                        ac.add(hasClass(line));
                    }
                }
            }

        }

        System.out.println("Modified classes: " + (int)mc.stream().distinct().count());
        System.out.println("Added classes: " + (int)ac.stream().distinct().count());
        System.out.println("Deleted classes: " + (int)dc.stream().distinct().count());

        List<String> mf = new ArrayList<>();
        List<String> af = new ArrayList<>();
        List<String> df = new ArrayList<>();

        for (ArrayList<String> fdarr: fileDiffs) {
            for (String line : fdarr) {
                if (!hasFunc(line).isBlank()) {
                    String f = "Function %s in file %s is %s";
                    int start = fdarr.indexOf(line) + 1;
                    StringBuilder status = new StringBuilder();
                    status.append(line);
                    while (start < fdarr.size() - 1) {
                        if (!fdarr.get(start).contains("return") || !hasFunc(fdarr.get(start)).isBlank()) {
                            status.append(fdarr.get(start));
                            start++;
                        } else {
                            break;
                        }
                    }
                    if (status.toString().contains("-") && status.toString().contains("+")) {
                        System.out.printf((f) + "%n", line.charAt(0) + hasFunc(line), fdarr.get(0), "modified");
                        mf.add(hasFunc(line));
                    } else if (status.toString().contains("-") && !status.toString().contains("+")) {
                        System.out.printf((f) + "%n", line.charAt(0) + hasFunc(line), fdarr.get(0), "deleted");
                        df.add(hasFunc(line));
                    } else if (!status.toString().contains("-") && status.toString().contains("+")) {
                        System.out.printf((f) + "%n", line.charAt(0) + hasFunc(line), fdarr.get(0), "added");
                        af.add(hasFunc(line));
                    }
                }
            }

        }

        System.out.println("Modified functions: " + (int)mf.stream().distinct().count());
        System.out.println("Added functions: " + (int)af.stream().distinct().count());
        System.out.println("Deleted functions: " + (int)df.stream().distinct().count());

        List<String> counter = new ArrayList<>();

        for (ArrayList<String> fdarr: fileDiffs) {
            StringBuilder sb = new StringBuilder();
            fdarr.forEach(sb::append);
            boolean isModule = hasFunc(sb.toString()).isBlank() && hasClass(sb.toString()).isBlank();
            if (isModule) {
                if (sb.toString().contains("-") || sb.toString().contains("+")) {
                    String f = "Module file %s is %s";
                    System.out.printf((f) + "%n", fdarr.get(0), "modified");
                    counter.add(fdarr.get(0));
                }
            }
        }

        System.out.println("Modified module: " + (int)counter.stream().distinct().count());


//        getRemoved("/Users/tshi/IdeaProjects/breachin/src/main/resources/pandas_remove");
    }

    public static String getValueByRegexPat(String inputStr, String regexPat) {
        String result = "";
        Pattern pat = Pattern.compile(regexPat, Pattern.CASE_INSENSITIVE);
        Matcher mat = pat.matcher(inputStr);
        if (mat.find()) result = mat.group(0);
        return result;
    }

    public static String hasClass(String str) {
        String classRegex = "class (\\w+)\\s*:";
        String classRegexParam = "class (\\w+)\\s*\\((.*?)\\):";
        String clazz = getValueByRegexPat(str, classRegex);
        String pClazz = getValueByRegexPat(str, classRegexParam);

        return clazz.isBlank() ? pClazz : clazz;
    }

    public static String hasFunc(String str) {
        String regex = "def (\\w+)\\s*\\((.*?)\\):";
        return getValueByRegexPat(str, regex);
    }

    public static void getRemoved(String path) throws IOException {
        List<String> classCount = new ArrayList<>();
        List<String> funcCount = new ArrayList<>();
        List<String> moduleCount = new ArrayList<>();

        List<String> collect = Files.readAllLines(Paths.get(path));

        collect.forEach(f -> {
//                System.out.println(f);
            if (f.endsWith(".py") && !f.contains("test") && !f.contains("doc") && !f.contains("example")) {
                try {
                    String content = GetAllCodeUnitsFromFolder.readFileToString(f);
                    if (!content.contains("class ") && !content.contains("def ")) {
                        System.out.println(" Module : " + f + "is deleted");
                        moduleCount.add(f);
                    }
                    Pattern MY_PATTERN = Pattern.compile("def (\\w+)\\s*\\((.*?)\\):");
                    Matcher m = MY_PATTERN.matcher(content);
                    while(m.find()) {
                        System.out.println(m.group() + " in file : " + f + "is deleted");
                        funcCount.add(m.group());
                    }
                    Pattern MY_PATTERN2 = Pattern.compile("class (\\w+)\\s*\\((.*?)\\):");
                    Matcher m2 = MY_PATTERN2.matcher(content);
                    while(m2.find()) {
                        System.out.println(m2.group() + " in file : " + f + "is deleted");
                        classCount.add(m2.group());
                    }
                    Pattern MY_PATTERN3 = Pattern.compile("class (\\w+)\\s*:");
                    Matcher m3 = MY_PATTERN3.matcher(content);
                    while(m3.find()) {
                        System.out.println(m3.group() + " in file : " + f + "is deleted");
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



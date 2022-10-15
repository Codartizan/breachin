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
public class App 
{
    public static void main( String[] args ) {
        String file = "/Users/tshi/IdeaProjects/breachin/src/main/resources/django_remained_diff";

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

        int mc = 0;
        int ac = 0;
        int dc = 0;

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
//                        System.out.printf((f) + "%n", line.charAt(0) + hasClass(line), fdarr.get(0), "modified");
                        mc++;
                    } else if (status.toString().contains("-") && !status.toString().contains("+")) {
//                        System.out.printf((f) + "%n", line.charAt(0) + hasClass(line), fdarr.get(0), "deleted");
                        dc++;
                    } else if (!status.toString().contains("-") && status.toString().contains("+")) {
//                        System.out.printf((f) + "%n", line.charAt(0) + hasClass(line), fdarr.get(0), "added");
                        ac++;
                    }
                }
            }

        }

        System.out.println("Modified classes: " + mc);
        System.out.println("Added classes: " + ac);
        System.out.println("Deleted classes: " + dc);

        int mf = 0;
        int af = 0;
        int df = 0;

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
//                        System.out.printf((f) + "%n", line.charAt(0) + hasFunc(line), fdarr.get(0), "modified");
                        mf++;
                    } else if (status.toString().contains("-") && !status.toString().contains("+")) {
//                        System.out.printf((f) + "%n", line.charAt(0) + hasFunc(line), fdarr.get(0), "deleted");
                        df++;
                    } else if (!status.toString().contains("-") && status.toString().contains("+")) {
//                        System.out.printf((f) + "%n", line.charAt(0) + hasFunc(line), fdarr.get(0), "added");
                        af++;
                    }
                }
            }

        }

        System.out.println("Modified functions: " + mf);
        System.out.println("Added functions: " + af);
        System.out.println("Deleted functions: " + df);

        int counter = 0;

        for (ArrayList<String> fdarr: fileDiffs) {
            StringBuilder sb = new StringBuilder();
            fdarr.forEach(sb::append);
            boolean isModule = hasFunc(sb.toString()).isBlank() && hasFunc(sb.toString()).isBlank();
            if (isModule) {
                if (sb.toString().contains("-") || sb.toString().contains("+")) {
                    String f = "Module file %s is %s";
//                    System.out.printf((f) + "%n", fdarr.get(0), "modified");
                    counter++;
                }
            }
        }

        System.out.println("Modified module: " + counter);
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
}

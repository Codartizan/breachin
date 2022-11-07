package org.example.searchCode;

import com.google.gson.annotations.SerializedName;

public class ItemsItem{

	@SerializedName("path")
	private String path;

	@SerializedName("score")
	private double score;

	@SerializedName("html_url")
	private String htmlUrl;

	@SerializedName("name")
	private String name;

	@SerializedName("git_url")
	private String gitUrl;

	@SerializedName("repository")
	private Repository repository;

	@SerializedName("sha")
	private String sha;

	@SerializedName("url")
	private String url;

	public String getPath(){
		return path;
	}

	public double getScore(){
		return score;
	}

	public String getHtmlUrl(){
		return htmlUrl;
	}

	public String getName(){
		return name;
	}

	public String getGitUrl(){
		return gitUrl;
	}

	public Repository getRepository(){
		return repository;
	}

	public String getSha(){
		return sha;
	}

	public String getUrl(){
		return url;
	}
}
package org.example.searchCode;

import com.google.gson.annotations.SerializedName;

public class Repository{

	@SerializedName("tags_url")
	private String tagsUrl;

	@SerializedName("private")
	private boolean jsonMemberPrivate;

	@SerializedName("contributors_url")
	private String contributorsUrl;

	@SerializedName("notifications_url")
	private String notificationsUrl;

	@SerializedName("description")
	private String description;

	@SerializedName("subscription_url")
	private String subscriptionUrl;

	@SerializedName("keys_url")
	private String keysUrl;

	@SerializedName("branches_url")
	private String branchesUrl;

	@SerializedName("deployments_url")
	private String deploymentsUrl;

	@SerializedName("issue_comment_url")
	private String issueCommentUrl;

	@SerializedName("labels_url")
	private String labelsUrl;

	@SerializedName("subscribers_url")
	private String subscribersUrl;

	@SerializedName("releases_url")
	private String releasesUrl;

	@SerializedName("comments_url")
	private String commentsUrl;

	@SerializedName("stargazers_url")
	private String stargazersUrl;

	@SerializedName("id")
	private int id;

	@SerializedName("owner")
	private Owner owner;

	@SerializedName("archive_url")
	private String archiveUrl;

	@SerializedName("commits_url")
	private String commitsUrl;

	@SerializedName("git_refs_url")
	private String gitRefsUrl;

	@SerializedName("forks_url")
	private String forksUrl;

	@SerializedName("compare_url")
	private String compareUrl;

	@SerializedName("statuses_url")
	private String statusesUrl;

	@SerializedName("git_commits_url")
	private String gitCommitsUrl;

	@SerializedName("blobs_url")
	private String blobsUrl;

	@SerializedName("git_tags_url")
	private String gitTagsUrl;

	@SerializedName("merges_url")
	private String mergesUrl;

	@SerializedName("downloads_url")
	private String downloadsUrl;

	@SerializedName("url")
	private String url;

	@SerializedName("contents_url")
	private String contentsUrl;

	@SerializedName("milestones_url")
	private String milestonesUrl;

	@SerializedName("teams_url")
	private String teamsUrl;

	@SerializedName("fork")
	private boolean fork;

	@SerializedName("issues_url")
	private String issuesUrl;

	@SerializedName("full_name")
	private String fullName;

	@SerializedName("events_url")
	private String eventsUrl;

	@SerializedName("issue_events_url")
	private String issueEventsUrl;

	@SerializedName("languages_url")
	private String languagesUrl;

	@SerializedName("html_url")
	private String htmlUrl;

	@SerializedName("collaborators_url")
	private String collaboratorsUrl;

	@SerializedName("name")
	private String name;

	@SerializedName("pulls_url")
	private String pullsUrl;

	@SerializedName("hooks_url")
	private String hooksUrl;

	@SerializedName("assignees_url")
	private String assigneesUrl;

	@SerializedName("trees_url")
	private String treesUrl;

	@SerializedName("node_id")
	private String nodeId;

	public String getTagsUrl(){
		return tagsUrl;
	}

	public boolean isJsonMemberPrivate(){
		return jsonMemberPrivate;
	}

	public String getContributorsUrl(){
		return contributorsUrl;
	}

	public String getNotificationsUrl(){
		return notificationsUrl;
	}

	public String getDescription(){
		return description;
	}

	public String getSubscriptionUrl(){
		return subscriptionUrl;
	}

	public String getKeysUrl(){
		return keysUrl;
	}

	public String getBranchesUrl(){
		return branchesUrl;
	}

	public String getDeploymentsUrl(){
		return deploymentsUrl;
	}

	public String getIssueCommentUrl(){
		return issueCommentUrl;
	}

	public String getLabelsUrl(){
		return labelsUrl;
	}

	public String getSubscribersUrl(){
		return subscribersUrl;
	}

	public String getReleasesUrl(){
		return releasesUrl;
	}

	public String getCommentsUrl(){
		return commentsUrl;
	}

	public String getStargazersUrl(){
		return stargazersUrl;
	}

	public int getId(){
		return id;
	}

	public Owner getOwner(){
		return owner;
	}

	public String getArchiveUrl(){
		return archiveUrl;
	}

	public String getCommitsUrl(){
		return commitsUrl;
	}

	public String getGitRefsUrl(){
		return gitRefsUrl;
	}

	public String getForksUrl(){
		return forksUrl;
	}

	public String getCompareUrl(){
		return compareUrl;
	}

	public String getStatusesUrl(){
		return statusesUrl;
	}

	public String getGitCommitsUrl(){
		return gitCommitsUrl;
	}

	public String getBlobsUrl(){
		return blobsUrl;
	}

	public String getGitTagsUrl(){
		return gitTagsUrl;
	}

	public String getMergesUrl(){
		return mergesUrl;
	}

	public String getDownloadsUrl(){
		return downloadsUrl;
	}

	public String getUrl(){
		return url;
	}

	public String getContentsUrl(){
		return contentsUrl;
	}

	public String getMilestonesUrl(){
		return milestonesUrl;
	}

	public String getTeamsUrl(){
		return teamsUrl;
	}

	public boolean isFork(){
		return fork;
	}

	public String getIssuesUrl(){
		return issuesUrl;
	}

	public String getFullName(){
		return fullName;
	}

	public String getEventsUrl(){
		return eventsUrl;
	}

	public String getIssueEventsUrl(){
		return issueEventsUrl;
	}

	public String getLanguagesUrl(){
		return languagesUrl;
	}

	public String getHtmlUrl(){
		return htmlUrl;
	}

	public String getCollaboratorsUrl(){
		return collaboratorsUrl;
	}

	public String getName(){
		return name;
	}

	public String getPullsUrl(){
		return pullsUrl;
	}

	public String getHooksUrl(){
		return hooksUrl;
	}

	public String getAssigneesUrl(){
		return assigneesUrl;
	}

	public String getTreesUrl(){
		return treesUrl;
	}

	public String getNodeId(){
		return nodeId;
	}
}
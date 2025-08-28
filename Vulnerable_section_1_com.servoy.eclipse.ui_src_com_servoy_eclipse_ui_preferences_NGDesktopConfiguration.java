 {
 
 	private static final String versionsUrl = "https://download.servoy.com/ngdesktop/ngdesktop-versions.txt";
	private static List<String> remoteVersions = new ArrayList<String>();
 
 	private Combo srcVersionCombo;
 	private Label deprecatedLabel;
 
 	public static List<String> getAvailableVersions()
 	{
 		try
 		{
 			final URL url = new URL(versionsUrl);
 					sb.append(line);
 				final JSONObject jsonObj = new JSONObject(sb.toString());
 				JSONArray releases = jsonObj.getJSONArray("releases");
				remoteVersions.clear();
 				for (int i = 0; i < releases.length(); i++)
 				{
 					JSONObject release = releases.getJSONObject(i);
					String servoyVersion = release.getString("servoy-version");
 
					// check if devVersion fits into the interval defined by servoyVersion
					String[] interval = servoyVersion.split("-"); // split the servoyVersion into start and end
 
					if (interval.length == 2)
					{
						if (SemVerComparator.compare(devVersion, interval[0]) >= 0 &&
							SemVerComparator.compare(devVersion, interval[1]) <= 0)
 						{
							remoteVersions.add(release.getString("version"));
 						}
					}
					else
					{
						if (SemVerComparator.compare(devVersion, servoyVersion) >= 0)
 						{
							remoteVersions.add(release.getString("version"));
 						}
 					}
 				}
 		return remoteVersions;
 	}
 
	private static String getBaseVersion(String version)
 	{
		String[] result = version.split("\\.");
		if (result.length <= 2) return version;
		return result[0] + "." + result[1];
 	}
 
 	@Override
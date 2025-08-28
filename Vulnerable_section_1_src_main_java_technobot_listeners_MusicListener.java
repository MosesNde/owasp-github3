 import org.jetbrains.annotations.Nullable;
 import technobot.data.GuildData;
 import technobot.handlers.MusicHandler;
 import technobot.util.embeds.EmbedColor;
 import technobot.util.embeds.EmbedUtils;
 
 import java.util.Objects;
 
 /**
         MusicHandler music = GuildData.get(event.getGuild()).musicHandler;
         if (music == null) return;
 
         playerManager.loadItem(url, new AudioLoadResultHandler() {
 
             @Override
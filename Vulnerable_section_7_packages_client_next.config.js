 
 // eslint-disable-next-line @typescript-eslint/no-var-requires
 const { composePlugins, withNx } = require('@nx/next');
 const { i18n } = require('./next-i18next.config');
 
 /**
  * @type {import('@nx/next/plugins/with-nx').WithNxOptions}
     locales: i18n.locales,
     defaultLocale: i18n.defaultLocale,
   },
 };
 
 const plugins = [
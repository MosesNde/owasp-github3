 //----------------------------------------------------------------------------
 std::ostream& Utils::operator<<(std::ostream& os, const Configuration& config)
 {
    os << "Config -----------" << std::endl
        << "point size : " << config.point_size << '\n'
        << "antialias  : " << (config.antialias ? "true" : "false") << '\n'
        << "motion blur: " << (config.motion_blur ? "true" : "false") << '\n'
       << "show trails: " << (config.show_trails ? "true" : "false") << std::endl;
 
     return os;
 }
         }
 
         if (ERROR_SUCCESS == readRegistryValue(KEY_PIXELSPERPOINT)) {
            config.show_trails = dataVal;
         }
 
         RegCloseKey(default_key);
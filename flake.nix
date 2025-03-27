{
  description = "Generic Raspberry Pi Pico development environment";

  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
  };

  outputs = { nixpkgs, ... }:
    let
      pkgs = nixpkgs.legacyPackages.x86_64-linux;
    in {
      devShells.x86_64-linux.default = pkgs.mkShell {
        buildInputs = with pkgs; [
          # Linux Host #
          python3
          python312Packages.pygobject3
          python312Packages.pygobject-stubs
          udisks

          # Pico Firmware #
          cmake
          gcc-arm-embedded
          picotool
          glibc_multi
          gobject-introspection
        ];

        shellHook = ''

        '';
      };
    };
}

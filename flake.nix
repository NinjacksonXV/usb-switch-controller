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
          cmake
          ninja
          gcc-arm-embedded
          python3
          git
          picotool
          glibc_multi
        ];

        shellHook = ''

        '';
      };
    };
}

// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { DevicePoolArgs } from "./devicePool";
export type DevicePool = import("./devicePool").DevicePool;
export const DevicePool: typeof import("./devicePool").DevicePool = null as any;
utilities.lazyLoad(exports, ["DevicePool"], () => require("./devicePool"));

export { GetDevicePoolArgs, GetDevicePoolResult, GetDevicePoolOutputArgs } from "./getDevicePool";
export const getDevicePool: typeof import("./getDevicePool").getDevicePool = null as any;
export const getDevicePoolOutput: typeof import("./getDevicePool").getDevicePoolOutput = null as any;
utilities.lazyLoad(exports, ["getDevicePool","getDevicePoolOutput"], () => require("./getDevicePool"));

export { GetInstanceProfileArgs, GetInstanceProfileResult, GetInstanceProfileOutputArgs } from "./getInstanceProfile";
export const getInstanceProfile: typeof import("./getInstanceProfile").getInstanceProfile = null as any;
export const getInstanceProfileOutput: typeof import("./getInstanceProfile").getInstanceProfileOutput = null as any;
utilities.lazyLoad(exports, ["getInstanceProfile","getInstanceProfileOutput"], () => require("./getInstanceProfile"));

export { GetNetworkProfileArgs, GetNetworkProfileResult, GetNetworkProfileOutputArgs } from "./getNetworkProfile";
export const getNetworkProfile: typeof import("./getNetworkProfile").getNetworkProfile = null as any;
export const getNetworkProfileOutput: typeof import("./getNetworkProfile").getNetworkProfileOutput = null as any;
utilities.lazyLoad(exports, ["getNetworkProfile","getNetworkProfileOutput"], () => require("./getNetworkProfile"));

export { GetProjectArgs, GetProjectResult, GetProjectOutputArgs } from "./getProject";
export const getProject: typeof import("./getProject").getProject = null as any;
export const getProjectOutput: typeof import("./getProject").getProjectOutput = null as any;
utilities.lazyLoad(exports, ["getProject","getProjectOutput"], () => require("./getProject"));

export { GetTestGridProjectArgs, GetTestGridProjectResult, GetTestGridProjectOutputArgs } from "./getTestGridProject";
export const getTestGridProject: typeof import("./getTestGridProject").getTestGridProject = null as any;
export const getTestGridProjectOutput: typeof import("./getTestGridProject").getTestGridProjectOutput = null as any;
utilities.lazyLoad(exports, ["getTestGridProject","getTestGridProjectOutput"], () => require("./getTestGridProject"));

export { GetVpceConfigurationArgs, GetVpceConfigurationResult, GetVpceConfigurationOutputArgs } from "./getVpceConfiguration";
export const getVpceConfiguration: typeof import("./getVpceConfiguration").getVpceConfiguration = null as any;
export const getVpceConfigurationOutput: typeof import("./getVpceConfiguration").getVpceConfigurationOutput = null as any;
utilities.lazyLoad(exports, ["getVpceConfiguration","getVpceConfigurationOutput"], () => require("./getVpceConfiguration"));

export { InstanceProfileArgs } from "./instanceProfile";
export type InstanceProfile = import("./instanceProfile").InstanceProfile;
export const InstanceProfile: typeof import("./instanceProfile").InstanceProfile = null as any;
utilities.lazyLoad(exports, ["InstanceProfile"], () => require("./instanceProfile"));

export { NetworkProfileArgs } from "./networkProfile";
export type NetworkProfile = import("./networkProfile").NetworkProfile;
export const NetworkProfile: typeof import("./networkProfile").NetworkProfile = null as any;
utilities.lazyLoad(exports, ["NetworkProfile"], () => require("./networkProfile"));

export { ProjectArgs } from "./project";
export type Project = import("./project").Project;
export const Project: typeof import("./project").Project = null as any;
utilities.lazyLoad(exports, ["Project"], () => require("./project"));

export { TestGridProjectArgs } from "./testGridProject";
export type TestGridProject = import("./testGridProject").TestGridProject;
export const TestGridProject: typeof import("./testGridProject").TestGridProject = null as any;
utilities.lazyLoad(exports, ["TestGridProject"], () => require("./testGridProject"));

export { VpceConfigurationArgs } from "./vpceConfiguration";
export type VpceConfiguration = import("./vpceConfiguration").VpceConfiguration;
export const VpceConfiguration: typeof import("./vpceConfiguration").VpceConfiguration = null as any;
utilities.lazyLoad(exports, ["VpceConfiguration"], () => require("./vpceConfiguration"));


// Export enums:
export * from "../types/enums/devicefarm";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:devicefarm:DevicePool":
                return new DevicePool(name, <any>undefined, { urn })
            case "aws-native:devicefarm:InstanceProfile":
                return new InstanceProfile(name, <any>undefined, { urn })
            case "aws-native:devicefarm:NetworkProfile":
                return new NetworkProfile(name, <any>undefined, { urn })
            case "aws-native:devicefarm:Project":
                return new Project(name, <any>undefined, { urn })
            case "aws-native:devicefarm:TestGridProject":
                return new TestGridProject(name, <any>undefined, { urn })
            case "aws-native:devicefarm:VpceConfiguration":
                return new VpceConfiguration(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "devicefarm", _module)

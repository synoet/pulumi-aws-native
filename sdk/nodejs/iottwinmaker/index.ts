// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { ComponentTypeArgs } from "./componentType";
export type ComponentType = import("./componentType").ComponentType;
export const ComponentType: typeof import("./componentType").ComponentType = null as any;
utilities.lazyLoad(exports, ["ComponentType"], () => require("./componentType"));

export { EntityArgs } from "./entity";
export type Entity = import("./entity").Entity;
export const Entity: typeof import("./entity").Entity = null as any;
utilities.lazyLoad(exports, ["Entity"], () => require("./entity"));

export { GetComponentTypeArgs, GetComponentTypeResult, GetComponentTypeOutputArgs } from "./getComponentType";
export const getComponentType: typeof import("./getComponentType").getComponentType = null as any;
export const getComponentTypeOutput: typeof import("./getComponentType").getComponentTypeOutput = null as any;
utilities.lazyLoad(exports, ["getComponentType","getComponentTypeOutput"], () => require("./getComponentType"));

export { GetEntityArgs, GetEntityResult, GetEntityOutputArgs } from "./getEntity";
export const getEntity: typeof import("./getEntity").getEntity = null as any;
export const getEntityOutput: typeof import("./getEntity").getEntityOutput = null as any;
utilities.lazyLoad(exports, ["getEntity","getEntityOutput"], () => require("./getEntity"));

export { GetSceneArgs, GetSceneResult, GetSceneOutputArgs } from "./getScene";
export const getScene: typeof import("./getScene").getScene = null as any;
export const getSceneOutput: typeof import("./getScene").getSceneOutput = null as any;
utilities.lazyLoad(exports, ["getScene","getSceneOutput"], () => require("./getScene"));

export { GetSyncJobArgs, GetSyncJobResult, GetSyncJobOutputArgs } from "./getSyncJob";
export const getSyncJob: typeof import("./getSyncJob").getSyncJob = null as any;
export const getSyncJobOutput: typeof import("./getSyncJob").getSyncJobOutput = null as any;
utilities.lazyLoad(exports, ["getSyncJob","getSyncJobOutput"], () => require("./getSyncJob"));

export { GetWorkspaceArgs, GetWorkspaceResult, GetWorkspaceOutputArgs } from "./getWorkspace";
export const getWorkspace: typeof import("./getWorkspace").getWorkspace = null as any;
export const getWorkspaceOutput: typeof import("./getWorkspace").getWorkspaceOutput = null as any;
utilities.lazyLoad(exports, ["getWorkspace","getWorkspaceOutput"], () => require("./getWorkspace"));

export { SceneArgs } from "./scene";
export type Scene = import("./scene").Scene;
export const Scene: typeof import("./scene").Scene = null as any;
utilities.lazyLoad(exports, ["Scene"], () => require("./scene"));

export { SyncJobArgs } from "./syncJob";
export type SyncJob = import("./syncJob").SyncJob;
export const SyncJob: typeof import("./syncJob").SyncJob = null as any;
utilities.lazyLoad(exports, ["SyncJob"], () => require("./syncJob"));

export { WorkspaceArgs } from "./workspace";
export type Workspace = import("./workspace").Workspace;
export const Workspace: typeof import("./workspace").Workspace = null as any;
utilities.lazyLoad(exports, ["Workspace"], () => require("./workspace"));


// Export enums:
export * from "../types/enums/iottwinmaker";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:iottwinmaker:ComponentType":
                return new ComponentType(name, <any>undefined, { urn })
            case "aws-native:iottwinmaker:Entity":
                return new Entity(name, <any>undefined, { urn })
            case "aws-native:iottwinmaker:Scene":
                return new Scene(name, <any>undefined, { urn })
            case "aws-native:iottwinmaker:SyncJob":
                return new SyncJob(name, <any>undefined, { urn })
            case "aws-native:iottwinmaker:Workspace":
                return new Workspace(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "iottwinmaker", _module)

// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

// Export members:
export { CacheClusterArgs } from "./cacheCluster";
export type CacheCluster = import("./cacheCluster").CacheCluster;
export const CacheCluster: typeof import("./cacheCluster").CacheCluster = null as any;
utilities.lazyLoad(exports, ["CacheCluster"], () => require("./cacheCluster"));

export { GetCacheClusterArgs, GetCacheClusterResult, GetCacheClusterOutputArgs } from "./getCacheCluster";
export const getCacheCluster: typeof import("./getCacheCluster").getCacheCluster = null as any;
export const getCacheClusterOutput: typeof import("./getCacheCluster").getCacheClusterOutput = null as any;
utilities.lazyLoad(exports, ["getCacheCluster","getCacheClusterOutput"], () => require("./getCacheCluster"));

export { GetGlobalReplicationGroupArgs, GetGlobalReplicationGroupResult, GetGlobalReplicationGroupOutputArgs } from "./getGlobalReplicationGroup";
export const getGlobalReplicationGroup: typeof import("./getGlobalReplicationGroup").getGlobalReplicationGroup = null as any;
export const getGlobalReplicationGroupOutput: typeof import("./getGlobalReplicationGroup").getGlobalReplicationGroupOutput = null as any;
utilities.lazyLoad(exports, ["getGlobalReplicationGroup","getGlobalReplicationGroupOutput"], () => require("./getGlobalReplicationGroup"));

export { GetParameterGroupArgs, GetParameterGroupResult, GetParameterGroupOutputArgs } from "./getParameterGroup";
export const getParameterGroup: typeof import("./getParameterGroup").getParameterGroup = null as any;
export const getParameterGroupOutput: typeof import("./getParameterGroup").getParameterGroupOutput = null as any;
utilities.lazyLoad(exports, ["getParameterGroup","getParameterGroupOutput"], () => require("./getParameterGroup"));

export { GetReplicationGroupArgs, GetReplicationGroupResult, GetReplicationGroupOutputArgs } from "./getReplicationGroup";
export const getReplicationGroup: typeof import("./getReplicationGroup").getReplicationGroup = null as any;
export const getReplicationGroupOutput: typeof import("./getReplicationGroup").getReplicationGroupOutput = null as any;
utilities.lazyLoad(exports, ["getReplicationGroup","getReplicationGroupOutput"], () => require("./getReplicationGroup"));

export { GetSecurityGroupArgs, GetSecurityGroupResult, GetSecurityGroupOutputArgs } from "./getSecurityGroup";
export const getSecurityGroup: typeof import("./getSecurityGroup").getSecurityGroup = null as any;
export const getSecurityGroupOutput: typeof import("./getSecurityGroup").getSecurityGroupOutput = null as any;
utilities.lazyLoad(exports, ["getSecurityGroup","getSecurityGroupOutput"], () => require("./getSecurityGroup"));

export { GetSecurityGroupIngressArgs, GetSecurityGroupIngressResult, GetSecurityGroupIngressOutputArgs } from "./getSecurityGroupIngress";
export const getSecurityGroupIngress: typeof import("./getSecurityGroupIngress").getSecurityGroupIngress = null as any;
export const getSecurityGroupIngressOutput: typeof import("./getSecurityGroupIngress").getSecurityGroupIngressOutput = null as any;
utilities.lazyLoad(exports, ["getSecurityGroupIngress","getSecurityGroupIngressOutput"], () => require("./getSecurityGroupIngress"));

export { GetSubnetGroupArgs, GetSubnetGroupResult, GetSubnetGroupOutputArgs } from "./getSubnetGroup";
export const getSubnetGroup: typeof import("./getSubnetGroup").getSubnetGroup = null as any;
export const getSubnetGroupOutput: typeof import("./getSubnetGroup").getSubnetGroupOutput = null as any;
utilities.lazyLoad(exports, ["getSubnetGroup","getSubnetGroupOutput"], () => require("./getSubnetGroup"));

export { GetUserArgs, GetUserResult, GetUserOutputArgs } from "./getUser";
export const getUser: typeof import("./getUser").getUser = null as any;
export const getUserOutput: typeof import("./getUser").getUserOutput = null as any;
utilities.lazyLoad(exports, ["getUser","getUserOutput"], () => require("./getUser"));

export { GetUserGroupArgs, GetUserGroupResult, GetUserGroupOutputArgs } from "./getUserGroup";
export const getUserGroup: typeof import("./getUserGroup").getUserGroup = null as any;
export const getUserGroupOutput: typeof import("./getUserGroup").getUserGroupOutput = null as any;
utilities.lazyLoad(exports, ["getUserGroup","getUserGroupOutput"], () => require("./getUserGroup"));

export { GlobalReplicationGroupArgs } from "./globalReplicationGroup";
export type GlobalReplicationGroup = import("./globalReplicationGroup").GlobalReplicationGroup;
export const GlobalReplicationGroup: typeof import("./globalReplicationGroup").GlobalReplicationGroup = null as any;
utilities.lazyLoad(exports, ["GlobalReplicationGroup"], () => require("./globalReplicationGroup"));

export { ParameterGroupArgs } from "./parameterGroup";
export type ParameterGroup = import("./parameterGroup").ParameterGroup;
export const ParameterGroup: typeof import("./parameterGroup").ParameterGroup = null as any;
utilities.lazyLoad(exports, ["ParameterGroup"], () => require("./parameterGroup"));

export { ReplicationGroupArgs } from "./replicationGroup";
export type ReplicationGroup = import("./replicationGroup").ReplicationGroup;
export const ReplicationGroup: typeof import("./replicationGroup").ReplicationGroup = null as any;
utilities.lazyLoad(exports, ["ReplicationGroup"], () => require("./replicationGroup"));

export { SecurityGroupArgs } from "./securityGroup";
export type SecurityGroup = import("./securityGroup").SecurityGroup;
export const SecurityGroup: typeof import("./securityGroup").SecurityGroup = null as any;
utilities.lazyLoad(exports, ["SecurityGroup"], () => require("./securityGroup"));

export { SecurityGroupIngressArgs } from "./securityGroupIngress";
export type SecurityGroupIngress = import("./securityGroupIngress").SecurityGroupIngress;
export const SecurityGroupIngress: typeof import("./securityGroupIngress").SecurityGroupIngress = null as any;
utilities.lazyLoad(exports, ["SecurityGroupIngress"], () => require("./securityGroupIngress"));

export { SubnetGroupArgs } from "./subnetGroup";
export type SubnetGroup = import("./subnetGroup").SubnetGroup;
export const SubnetGroup: typeof import("./subnetGroup").SubnetGroup = null as any;
utilities.lazyLoad(exports, ["SubnetGroup"], () => require("./subnetGroup"));

export { UserArgs } from "./user";
export type User = import("./user").User;
export const User: typeof import("./user").User = null as any;
utilities.lazyLoad(exports, ["User"], () => require("./user"));

export { UserGroupArgs } from "./userGroup";
export type UserGroup = import("./userGroup").UserGroup;
export const UserGroup: typeof import("./userGroup").UserGroup = null as any;
utilities.lazyLoad(exports, ["UserGroup"], () => require("./userGroup"));


// Export enums:
export * from "../types/enums/elasticache";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "aws-native:elasticache:CacheCluster":
                return new CacheCluster(name, <any>undefined, { urn })
            case "aws-native:elasticache:GlobalReplicationGroup":
                return new GlobalReplicationGroup(name, <any>undefined, { urn })
            case "aws-native:elasticache:ParameterGroup":
                return new ParameterGroup(name, <any>undefined, { urn })
            case "aws-native:elasticache:ReplicationGroup":
                return new ReplicationGroup(name, <any>undefined, { urn })
            case "aws-native:elasticache:SecurityGroup":
                return new SecurityGroup(name, <any>undefined, { urn })
            case "aws-native:elasticache:SecurityGroupIngress":
                return new SecurityGroupIngress(name, <any>undefined, { urn })
            case "aws-native:elasticache:SubnetGroup":
                return new SubnetGroup(name, <any>undefined, { urn })
            case "aws-native:elasticache:User":
                return new User(name, <any>undefined, { urn })
            case "aws-native:elasticache:UserGroup":
                return new UserGroup(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("aws-native", "elasticache", _module)

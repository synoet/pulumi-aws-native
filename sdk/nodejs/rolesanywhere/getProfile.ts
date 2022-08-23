// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Definition of AWS::RolesAnywhere::Profile Resource Type
 */
export function getProfile(args: GetProfileArgs, opts?: pulumi.InvokeOptions): Promise<GetProfileResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:rolesanywhere:getProfile", {
        "profileId": args.profileId,
    }, opts);
}

export interface GetProfileArgs {
    profileId: string;
}

export interface GetProfileResult {
    readonly durationSeconds?: number;
    readonly enabled?: boolean;
    readonly managedPolicyArns?: string[];
    readonly name?: string;
    readonly profileArn?: string;
    readonly profileId?: string;
    readonly requireInstanceProperties?: boolean;
    readonly roleArns?: string[];
    readonly sessionPolicy?: string;
    readonly tags?: outputs.rolesanywhere.ProfileTag[];
}

export function getProfileOutput(args: GetProfileOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetProfileResult> {
    return pulumi.output(args).apply(a => getProfile(a, opts))
}

export interface GetProfileOutputArgs {
    profileId: pulumi.Input<string>;
}

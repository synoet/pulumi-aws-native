// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Cognito::UserPoolClient
 */
export function getUserPoolClient(args: GetUserPoolClientArgs, opts?: pulumi.InvokeOptions): Promise<GetUserPoolClientResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:cognito:getUserPoolClient", {
        "clientId": args.clientId,
        "userPoolId": args.userPoolId,
    }, opts);
}

export interface GetUserPoolClientArgs {
    clientId: string;
    userPoolId: string;
}

export interface GetUserPoolClientResult {
    readonly accessTokenValidity?: number;
    readonly allowedOAuthFlows?: string[];
    readonly allowedOAuthFlowsUserPoolClient?: boolean;
    readonly allowedOAuthScopes?: string[];
    readonly analyticsConfiguration?: outputs.cognito.UserPoolClientAnalyticsConfiguration;
    readonly authSessionValidity?: number;
    readonly callbackUrls?: string[];
    readonly clientId?: string;
    readonly clientName?: string;
    readonly clientSecret?: string;
    readonly defaultRedirectUri?: string;
    readonly enablePropagateAdditionalUserContextData?: boolean;
    readonly enableTokenRevocation?: boolean;
    readonly explicitAuthFlows?: string[];
    readonly idTokenValidity?: number;
    readonly logoutUrls?: string[];
    readonly name?: string;
    readonly preventUserExistenceErrors?: string;
    readonly readAttributes?: string[];
    readonly refreshTokenValidity?: number;
    readonly supportedIdentityProviders?: string[];
    readonly tokenValidityUnits?: outputs.cognito.UserPoolClientTokenValidityUnits;
    readonly writeAttributes?: string[];
}
/**
 * Resource Type definition for AWS::Cognito::UserPoolClient
 */
export function getUserPoolClientOutput(args: GetUserPoolClientOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetUserPoolClientResult> {
    return pulumi.output(args).apply((a: any) => getUserPoolClient(a, opts))
}

export interface GetUserPoolClientOutputArgs {
    clientId: pulumi.Input<string>;
    userPoolId: pulumi.Input<string>;
}

// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ServiceCatalog::PortfolioShare
 */
export function getPortfolioShare(args: GetPortfolioShareArgs, opts?: pulumi.InvokeOptions): Promise<GetPortfolioShareResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:servicecatalog:getPortfolioShare", {
        "id": args.id,
    }, opts);
}

export interface GetPortfolioShareArgs {
    id: string;
}

export interface GetPortfolioShareResult {
    readonly id?: string;
    readonly shareTagOptions?: boolean;
}
/**
 * Resource Type definition for AWS::ServiceCatalog::PortfolioShare
 */
export function getPortfolioShareOutput(args: GetPortfolioShareOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPortfolioShareResult> {
    return pulumi.output(args).apply((a: any) => getPortfolioShare(a, opts))
}

export interface GetPortfolioShareOutputArgs {
    id: pulumi.Input<string>;
}

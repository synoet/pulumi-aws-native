// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Version: None. Resource Type definition for AWS::DynamoDB::Table
 */
export function getTable(args: GetTableArgs, opts?: pulumi.InvokeOptions): Promise<GetTableResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:dynamodb:getTable", {
        "tableName": args.tableName,
    }, opts);
}

export interface GetTableArgs {
    tableName: string;
}

export interface GetTableResult {
    readonly arn?: string;
    readonly attributeDefinitions?: outputs.dynamodb.TableAttributeDefinition[];
    readonly billingMode?: string;
    readonly contributorInsightsSpecification?: outputs.dynamodb.TableContributorInsightsSpecification;
    readonly globalSecondaryIndexes?: outputs.dynamodb.TableGlobalSecondaryIndex[];
    readonly keySchema?: outputs.dynamodb.TableKeySchema[] | any;
    readonly kinesisStreamSpecification?: outputs.dynamodb.TableKinesisStreamSpecification;
    readonly localSecondaryIndexes?: outputs.dynamodb.TableLocalSecondaryIndex[];
    readonly pointInTimeRecoverySpecification?: outputs.dynamodb.TablePointInTimeRecoverySpecification;
    readonly provisionedThroughput?: outputs.dynamodb.TableProvisionedThroughput;
    readonly sSESpecification?: outputs.dynamodb.TableSSESpecification;
    readonly streamArn?: string;
    readonly streamSpecification?: outputs.dynamodb.TableStreamSpecification;
    readonly tableClass?: string;
    readonly tags?: outputs.dynamodb.TableTag[];
    readonly timeToLiveSpecification?: outputs.dynamodb.TableTimeToLiveSpecification;
}

export function getTableOutput(args: GetTableOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetTableResult> {
    return pulumi.output(args).apply(a => getTable(a, opts))
}

export interface GetTableOutputArgs {
    tableName: pulumi.Input<string>;
}

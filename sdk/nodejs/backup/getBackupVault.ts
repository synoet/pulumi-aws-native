// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Backup::BackupVault
 */
export function getBackupVault(args: GetBackupVaultArgs, opts?: pulumi.InvokeOptions): Promise<GetBackupVaultResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:backup:getBackupVault", {
        "backupVaultName": args.backupVaultName,
    }, opts);
}

export interface GetBackupVaultArgs {
    backupVaultName: string;
}

export interface GetBackupVaultResult {
    readonly accessPolicy?: any;
    readonly backupVaultArn?: string;
    readonly backupVaultTags?: any;
    readonly lockConfiguration?: outputs.backup.BackupVaultLockConfigurationType;
    readonly notifications?: outputs.backup.BackupVaultNotificationObjectType;
}
/**
 * Resource Type definition for AWS::Backup::BackupVault
 */
export function getBackupVaultOutput(args: GetBackupVaultOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetBackupVaultResult> {
    return pulumi.output(args).apply((a: any) => getBackupVault(a, opts))
}

export interface GetBackupVaultOutputArgs {
    backupVaultName: pulumi.Input<string>;
}

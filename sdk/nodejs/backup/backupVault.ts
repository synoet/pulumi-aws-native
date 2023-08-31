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
export class BackupVault extends pulumi.CustomResource {
    /**
     * Get an existing BackupVault resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): BackupVault {
        return new BackupVault(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:backup:BackupVault';

    /**
     * Returns true if the given object is an instance of BackupVault.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is BackupVault {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === BackupVault.__pulumiType;
    }

    public readonly accessPolicy!: pulumi.Output<any | undefined>;
    public /*out*/ readonly backupVaultArn!: pulumi.Output<string>;
    public readonly backupVaultName!: pulumi.Output<string>;
    public readonly backupVaultTags!: pulumi.Output<any | undefined>;
    public readonly encryptionKeyArn!: pulumi.Output<string | undefined>;
    public readonly lockConfiguration!: pulumi.Output<outputs.backup.BackupVaultLockConfigurationType | undefined>;
    public readonly notifications!: pulumi.Output<outputs.backup.BackupVaultNotificationObjectType | undefined>;

    /**
     * Create a BackupVault resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: BackupVaultArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["accessPolicy"] = args ? args.accessPolicy : undefined;
            resourceInputs["backupVaultName"] = args ? args.backupVaultName : undefined;
            resourceInputs["backupVaultTags"] = args ? args.backupVaultTags : undefined;
            resourceInputs["encryptionKeyArn"] = args ? args.encryptionKeyArn : undefined;
            resourceInputs["lockConfiguration"] = args ? args.lockConfiguration : undefined;
            resourceInputs["notifications"] = args ? args.notifications : undefined;
            resourceInputs["backupVaultArn"] = undefined /*out*/;
        } else {
            resourceInputs["accessPolicy"] = undefined /*out*/;
            resourceInputs["backupVaultArn"] = undefined /*out*/;
            resourceInputs["backupVaultName"] = undefined /*out*/;
            resourceInputs["backupVaultTags"] = undefined /*out*/;
            resourceInputs["encryptionKeyArn"] = undefined /*out*/;
            resourceInputs["lockConfiguration"] = undefined /*out*/;
            resourceInputs["notifications"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["backupVaultName", "encryptionKeyArn"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(BackupVault.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a BackupVault resource.
 */
export interface BackupVaultArgs {
    accessPolicy?: any;
    backupVaultName?: pulumi.Input<string>;
    backupVaultTags?: any;
    encryptionKeyArn?: pulumi.Input<string>;
    lockConfiguration?: pulumi.Input<inputs.backup.BackupVaultLockConfigurationTypeArgs>;
    notifications?: pulumi.Input<inputs.backup.BackupVaultNotificationObjectTypeArgs>;
}

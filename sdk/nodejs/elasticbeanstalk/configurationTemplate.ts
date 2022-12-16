// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ElasticBeanstalk::ConfigurationTemplate
 */
export class ConfigurationTemplate extends pulumi.CustomResource {
    /**
     * Get an existing ConfigurationTemplate resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ConfigurationTemplate {
        return new ConfigurationTemplate(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:elasticbeanstalk:ConfigurationTemplate';

    /**
     * Returns true if the given object is an instance of ConfigurationTemplate.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ConfigurationTemplate {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ConfigurationTemplate.__pulumiType;
    }

    /**
     * The name of the Elastic Beanstalk application to associate with this configuration template. 
     */
    public readonly applicationName!: pulumi.Output<string>;
    /**
     * An optional description for this configuration.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * The ID of an environment whose settings you want to use to create the configuration template. You must specify EnvironmentId if you don't specify PlatformArn, SolutionStackName, or SourceConfiguration. 
     */
    public readonly environmentId!: pulumi.Output<string | undefined>;
    /**
     * Option values for the Elastic Beanstalk configuration, such as the instance type. If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see [Option Values](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html) in the AWS Elastic Beanstalk Developer Guide. 
     */
    public readonly optionSettings!: pulumi.Output<outputs.elasticbeanstalk.ConfigurationTemplateConfigurationOptionSetting[] | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the custom platform. For more information, see [Custom Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html) in the AWS Elastic Beanstalk Developer Guide. 
     */
    public readonly platformArn!: pulumi.Output<string | undefined>;
    /**
     * The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, 64bit Amazon Linux 2013.09 running Tomcat 7 Java 7. A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see [Supported Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html) in the AWS Elastic Beanstalk Developer Guide.
     *
     *  You must specify SolutionStackName if you don't specify PlatformArn, EnvironmentId, or SourceConfiguration.
     *
     *  Use the ListAvailableSolutionStacks API to obtain a list of available solution stacks. 
     */
    public readonly solutionStackName!: pulumi.Output<string | undefined>;
    /**
     * An Elastic Beanstalk configuration template to base this one on. If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.
     *
     * Values specified in OptionSettings override any values obtained from the SourceConfiguration.
     *
     * You must specify SourceConfiguration if you don't specify PlatformArn, EnvironmentId, or SolutionStackName.
     *
     * Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name. 
     */
    public readonly sourceConfiguration!: pulumi.Output<outputs.elasticbeanstalk.ConfigurationTemplateSourceConfiguration | undefined>;
    /**
     * The name of the configuration template
     */
    public /*out*/ readonly templateName!: pulumi.Output<string>;

    /**
     * Create a ConfigurationTemplate resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ConfigurationTemplateArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.applicationName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'applicationName'");
            }
            resourceInputs["applicationName"] = args ? args.applicationName : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["environmentId"] = args ? args.environmentId : undefined;
            resourceInputs["optionSettings"] = args ? args.optionSettings : undefined;
            resourceInputs["platformArn"] = args ? args.platformArn : undefined;
            resourceInputs["solutionStackName"] = args ? args.solutionStackName : undefined;
            resourceInputs["sourceConfiguration"] = args ? args.sourceConfiguration : undefined;
            resourceInputs["templateName"] = undefined /*out*/;
        } else {
            resourceInputs["applicationName"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["environmentId"] = undefined /*out*/;
            resourceInputs["optionSettings"] = undefined /*out*/;
            resourceInputs["platformArn"] = undefined /*out*/;
            resourceInputs["solutionStackName"] = undefined /*out*/;
            resourceInputs["sourceConfiguration"] = undefined /*out*/;
            resourceInputs["templateName"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ConfigurationTemplate.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a ConfigurationTemplate resource.
 */
export interface ConfigurationTemplateArgs {
    /**
     * The name of the Elastic Beanstalk application to associate with this configuration template. 
     */
    applicationName: pulumi.Input<string>;
    /**
     * An optional description for this configuration.
     */
    description?: pulumi.Input<string>;
    /**
     * The ID of an environment whose settings you want to use to create the configuration template. You must specify EnvironmentId if you don't specify PlatformArn, SolutionStackName, or SourceConfiguration. 
     */
    environmentId?: pulumi.Input<string>;
    /**
     * Option values for the Elastic Beanstalk configuration, such as the instance type. If specified, these values override the values obtained from the solution stack or the source configuration template. For a complete list of Elastic Beanstalk configuration options, see [Option Values](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/command-options.html) in the AWS Elastic Beanstalk Developer Guide. 
     */
    optionSettings?: pulumi.Input<pulumi.Input<inputs.elasticbeanstalk.ConfigurationTemplateConfigurationOptionSettingArgs>[]>;
    /**
     * The Amazon Resource Name (ARN) of the custom platform. For more information, see [Custom Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/custom-platforms.html) in the AWS Elastic Beanstalk Developer Guide. 
     */
    platformArn?: pulumi.Input<string>;
    /**
     * The name of an Elastic Beanstalk solution stack (platform version) that this configuration uses. For example, 64bit Amazon Linux 2013.09 running Tomcat 7 Java 7. A solution stack specifies the operating system, runtime, and application server for a configuration template. It also determines the set of configuration options as well as the possible and default values. For more information, see [Supported Platforms](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts.platforms.html) in the AWS Elastic Beanstalk Developer Guide.
     *
     *  You must specify SolutionStackName if you don't specify PlatformArn, EnvironmentId, or SourceConfiguration.
     *
     *  Use the ListAvailableSolutionStacks API to obtain a list of available solution stacks. 
     */
    solutionStackName?: pulumi.Input<string>;
    /**
     * An Elastic Beanstalk configuration template to base this one on. If specified, Elastic Beanstalk uses the configuration values from the specified configuration template to create a new configuration.
     *
     * Values specified in OptionSettings override any values obtained from the SourceConfiguration.
     *
     * You must specify SourceConfiguration if you don't specify PlatformArn, EnvironmentId, or SolutionStackName.
     *
     * Constraint: If both solution stack name and source configuration are specified, the solution stack of the source configuration template must match the specified solution stack name. 
     */
    sourceConfiguration?: pulumi.Input<inputs.elasticbeanstalk.ConfigurationTemplateSourceConfigurationArgs>;
}

// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package gamecast

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Definition of AWS::GameCast::Application Resource Type
func LookupApplication(ctx *pulumi.Context, args *LookupApplicationArgs, opts ...pulumi.InvokeOption) (*LookupApplicationResult, error) {
	var rv LookupApplicationResult
	err := ctx.Invoke("aws-native:gamecast:getApplication", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupApplicationArgs struct {
	// ARN of the resource.
	Arn string `pulumi:"arn"`
}

type LookupApplicationResult struct {
	// ARN of the resource.
	Arn *string `pulumi:"arn"`
	// Descriptive label for the resource, not a unique ID.
	Description *string `pulumi:"description"`
	// Executable path is a relative path to the game launcher executable.
	ExecutablePath *string `pulumi:"executablePath"`
	// GameCast resource ID, base62 encoded.
	Id *string `pulumi:"id"`
	// A list of save file, registry key or log paths that are absolute paths that store game save files when the games
	// are running on a Windows environment.
	LogLocations      []string                      `pulumi:"logLocations"`
	SaveConfiguration *ApplicationSaveConfiguration `pulumi:"saveConfiguration"`
	Tags              *ApplicationTags              `pulumi:"tags"`
}

func LookupApplicationOutput(ctx *pulumi.Context, args LookupApplicationOutputArgs, opts ...pulumi.InvokeOption) LookupApplicationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupApplicationResult, error) {
			args := v.(LookupApplicationArgs)
			r, err := LookupApplication(ctx, &args, opts...)
			var s LookupApplicationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupApplicationResultOutput)
}

type LookupApplicationOutputArgs struct {
	// ARN of the resource.
	Arn pulumi.StringInput `pulumi:"arn"`
}

func (LookupApplicationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupApplicationArgs)(nil)).Elem()
}

type LookupApplicationResultOutput struct{ *pulumi.OutputState }

func (LookupApplicationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupApplicationResult)(nil)).Elem()
}

func (o LookupApplicationResultOutput) ToLookupApplicationResultOutput() LookupApplicationResultOutput {
	return o
}

func (o LookupApplicationResultOutput) ToLookupApplicationResultOutputWithContext(ctx context.Context) LookupApplicationResultOutput {
	return o
}

// ARN of the resource.
func (o LookupApplicationResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApplicationResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

// Descriptive label for the resource, not a unique ID.
func (o LookupApplicationResultOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApplicationResult) *string { return v.Description }).(pulumi.StringPtrOutput)
}

// Executable path is a relative path to the game launcher executable.
func (o LookupApplicationResultOutput) ExecutablePath() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApplicationResult) *string { return v.ExecutablePath }).(pulumi.StringPtrOutput)
}

// GameCast resource ID, base62 encoded.
func (o LookupApplicationResultOutput) Id() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupApplicationResult) *string { return v.Id }).(pulumi.StringPtrOutput)
}

// A list of save file, registry key or log paths that are absolute paths that store game save files when the games
// are running on a Windows environment.
func (o LookupApplicationResultOutput) LogLocations() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupApplicationResult) []string { return v.LogLocations }).(pulumi.StringArrayOutput)
}

func (o LookupApplicationResultOutput) SaveConfiguration() ApplicationSaveConfigurationPtrOutput {
	return o.ApplyT(func(v LookupApplicationResult) *ApplicationSaveConfiguration { return v.SaveConfiguration }).(ApplicationSaveConfigurationPtrOutput)
}

func (o LookupApplicationResultOutput) Tags() ApplicationTagsPtrOutput {
	return o.ApplyT(func(v LookupApplicationResult) *ApplicationTags { return v.Tags }).(ApplicationTagsPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupApplicationResultOutput{})
}
